from flask import Flask, Response, json, render_template, send_from_directory

from couchbase.bucket import Bucket as CBClient
from couchbase.n1ql import N1QLQuery
from couchbase.exceptions import NotFoundError, HTTPError

from constants import COUCHBASE_CONNECTION_STRING, COUCHBASE_BUCKET
from couchbase_utils import get_bucket_stats

app = Flask(__name__)
cb_client = CBClient(COUCHBASE_CONNECTION_STRING)


@app.route("/summary")
def summary():
    return render_template('template.html')


@app.route("/couchbase_summary")
def show_couchbase_summary():
    try:
    # get last inserted document by timestamp
        last_inserted_query = N1QLQuery('SELECT * FROM %s ORDER BY timestamp ASC default LIMIT 1;' % COUCHBASE_BUCKET)
        last_document = cb_client.n1ql_query(last_inserted_query).get_single_result()
    except HTTPError:
        last_document = None
  
    # get bucket document number
    stats = get_bucket_stats()
    documents_num = stats['itemCount'] 

    # get strongest relation between terms
    strongest_rel_query = N1QLQuery('SELECT * FROM %s WHERE related_terms' % COUCHBASE_BUCKET)
    strongest_rel_terms = []
    couchbase_summary = {
        "documents_num": documents_num,
        "last_document": last_document,
        "strongest_rel_terms": strongest_rel_terms
    }
    return Response(json.dumps(couchbase_summary))


@app.route('/scraper_summary')
def show_scraper_summary():
    try:
        scraper_summary = cb_client.get('scraper_summary').value
    except NotFoundError:
        scraper_summary = None
    return Response(json.dumps(scraper_summary))


@app.route('/js/<path:path>')
def staticjs(path):
    return send_from_directory('js', path)


@app.route('/css/<path:path>')
def staticcss(path):
    return send_from_directory('css', path)

@app.route('/img/<path:path>')
def staticimg(path):
    return send_from_directory('img', path)
