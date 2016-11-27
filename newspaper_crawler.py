import re
import uuid
import collections
import time

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
from newspaper_sources import (POLITICS_NEWSPAPERS, ECONOMY_NEWSPAPERS, SPORTS_NEWSPAPERS,
    TECH_NEWSPAPERS, CULTURE_NEWSPAPERS, SOURCE_NEWSPAPERS, TOPIC_TO_SOURCES)
from w3lib.html import remove_tags, remove_tags_with_content
from couchbase.bucket import Bucket as CBClient
from couchbase.exceptions import NotFoundError

from constants import COUCHBASE_CONNECTION_STRING

cb_client = CBClient(COUCHBASE_CONNECTION_STRING)


class NewspaperCrawler(CrawlSpider):

    name='newspaper_crawler',

    def __init__(self, topic=None, newspaper=None, term='', *args, **kwargs):
        self.term = term
        if newspaper:
            sources = [source for source in SOURCE_NEWSPAPERS if newspaper == source['name']]
        else:
            sources = TOPIC_TO_SOURCES.get(topic, SOURCE_NEWSPAPERS)
        self.allowed_domains = [source['allowed_domains'] for source in sources]
        self.start_urls = [source['url'] for source in sources]
        self.rules = []
        for source in sources:
            if topic:
                allowed_domain_regex=(source['allowed_subdomains_regex'][topic], )
            else:
               allowed_domain_regex = (regexsubdomain for topic, regexsubdomain in source['allowed_subdomains_regex'].items())
            rule = Rule(link_extractor=LinkExtractor(allow=allowed_domain_regex), 
                                                     callback='parse_with_term',
                                                     cb_kwargs={
                                                         'term': self.term,
                                                         'newspaper': newspaper
                                                     },
                                                     follow=True)
            self.rules.append(rule)

        return super(NewspaperCrawler, self).__init__(*args, **kwargs)

    def parse_with_term(self, response, term, newspaper):
        # clean response from scripts 
        response_content = remove_tags_with_content(response.text, ('script', 'a',  ))
        selector = Selector(text=response_content)
        term_query = '//body//*[contains(text(), "%s")]/text()' % self.term
        term_nodes = selector.select(term_query).extract()
        if not term_nodes:
            return
        
        item = {
            'url': response.url,
            'newspaper': newspaper,
            'term': term,
            'response_content': response.text,
            'timestamp': time.time()
        }

        related_terms = self.get_related_terms(term_nodes)
        if term in related_terms:
            related_terms.pop(term)
        item['related_terms'] = dict(related_terms)

        #with open(self.term, 'a') as content_file:
        #    content_file.write("%s\n" % item)
        cb_client.insert(str(uuid.uuid4()), item)

        # update scraper process
        self.update_scraper_summary(item)
        return item 

    def get_related_terms(self, term_nodes):   
        total_related_terms = collections.Counter()
        for node in term_nodes:
            related_terms = re.findall('[A-Z][a-z]{3,10}', node)
            total_related_terms += collections.Counter(related_terms)

        return total_related_terms

    def update_scraper_summary(self, item):
        newspaper = item['newspaper']

        try:
            scraper_summary = cb_client.get("scraper_summary").value

            scraper_summary['scraped_num'] += 1
            scraper_summary['last_site'] = item['newspaper']
            scraper_summary['last_site_url'] = item['url']
            scraper_summary['last_term'] = item['term']
            if newspaper in scraper_summary['scraped_newspaper_num']:
                scraper_summary['scraped_newspaper_num'][newspaper] +=1
            else:
                scraper_summary['scraped_newspaper_num'][newspaper] =1
            cb_client.upsert('scraper_summary', scraper_summary)
        except NotFoundError:
            scraper_summary = {
                'scraped_num': 1,
                'last_site': item['newspaper'],
                'last_site_url': item['url'],
                'last_term': item['term'],
                'scraped_newspaper_num': {
                    newspaper: 1
                } 
            }
            cb_client.insert('scraper_summary', scraper_summary)
