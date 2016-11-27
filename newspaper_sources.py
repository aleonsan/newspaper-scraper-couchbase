SOURCE_NEWSPAPERS = [
    { 
        'name': 'El mundo',
        'url': 'http://www.elmundo.es',
        'allowed_domains': 'elmundo.es',
        'allowed_subdomains_regex': {
            'politics': '.*elmundo.es/[espana|internacional].*',
            'economy': '.*elmundo.es/economia.*',
            'sports': '.*elmundo.es/deportes.*',
            'tech': '.*elmundo.es/tecnologia.*',
            'culture': '.*elmundo.es/cultura.*'
        }
    },
    { 
        'name': 'El pais', 
        'url': 'http://www.elpais.com',
        'allowed_domains': 'elpais.com',
        'allowed_subdomains_regex': {
            'politics': '.*politica.elpais.com/politica.*',
            'economy': '.*economia.elpais.com/economia.*',
            'sports': '.*deportes.elpais.com/deportes.*',
            'tech': '.*tecnologia.elpais.com/tecnologia.*',
            'culture': '.*cultura.elpais.com/cultura.*',
        }
    },
    {
        'name': 'ABC', 
        'url': 'http://www.abc.es',
        'allowed_domains': 'abc.es',
        'allowed_subdomains_regex': {
            'politics': '.*abc.es/[espana|internacional].*',
            'economy': '.*abc.es/economia.*',
            'sports': '.*abc.es/deportes.*',
            'culture': '.*abc.es/cultura.*',
        }
    },
    {
        'name': 'El confidencial', 
        'url': 'http://www.elconfidencial.com',
        'allowed_domains': 'elconfidencial.com',
        'allowed_subdomains_regex': {
            'politics': '.*elconfidencial.com/[espana|mundo].*',
            'economy': '.*elconfidencial.com/economia.*',
            'sports': '.*elconfidencial.com/deportes.*',
            'tech': '.*elconfidencial.com/tecnologia.*',
            'culture': '.*elconfidencial.com/cultura.*',
        }
    },
    { 
        'name': 'Diario publico',
        'url': 'http://www.publico.es',
        'allowed_domains': 'publico.es',
        'allowed_subdomains_regex': {
            'politics': '.*publico.es/politica.*',
            'economy': '.*publico.es/economia.*',
            'sports': '.*publico.es/deportes.*',
            'culture': '.*publico.es/culturas.*',
        }
    },
    { 
        'name': 'Marca',
        'url': 'http://www.marca.com',
        'allowed_domains': 'marca.com',
        'allowed_subdomains_regex': {
            'sports': '.*marca.com.*',
        }
    },
    {
        'name': 'Genbeta',
        'url': 'http://www.genbeta.com',
        'allowed_domains': 'genbeta.com',
        'allowed_subdomains_regex': {
            'tech': '.*genbeta.com.*',
        }
    },
    { 
        'name': 'El periodico',
        'url': 'http://www.elperiodico.com', 
        'allowed_domains': 'elperiodico.com',
        'allowed_subdomains_regex': {
            'politics': '.*elperiodico.com/es/[politica|internacional].*',
            'economy': '.*elperiodico.com/es/economia.*',
            'sports': '.*elperiodico.com/es/deportes.*',
            'culture': '.*elperiodico.com/es/ocio-y-cultura.*'
        }
    },
    { 
        'name': 'La vanguardia',
        'url': 'http://www.lavanguardia.com', 
        'allowed_domains': 'lavanguardia.com',
        'allowed_subdomains_regex': {
            'politics': '.*elperiodico.com/es/[politica|internacional].*',
            'economy': '.*elperiodico.com/es/economia.*',
            'sports': '.*elperiodico.com/es/deportes.*',
            'culture': '.*elperiodico.com/es/ocio-y-cultura.*'
        }
    },
    { 
        'name': 'El correo',
#        'url': 'http://www.', 
        'allowed_domains': 'lavanguardia.com',
        'allowed_subdomains_regex': {
#            'tech': '.*genbeta.com.*',
        }
    },
#    { 'name': 'elcorreo.com', 
#    { 'name': 'diariovasco.com', 
#    { 'name': 'okdiario.com', 
#    'expansion.com',
#    'cincodías.com', 
#    'as.com', 
#    'sport.com', 
#    'mundodeportivo.com', 
#    'eldesmarque.es', 
#    'genbeta.com', 
#    'xataka.com', 
#    'bitelia.com', 
#    'diarioti.com', 
#    'noticiasdelaciencia.com', 
#    'laflecha.net'

]

POLITICS_NEWSPAPERS = filter(lambda x: 'politics' in x['allowed_subdomains_regex'], SOURCE_NEWSPAPERS) 
ECONOMY_NEWSPAPERS = filter(lambda x: 'economy' in x['allowed_subdomains_regex'], SOURCE_NEWSPAPERS)
SPORTS_NEWSPAPERS = filter(lambda x: 'sports' in x['allowed_subdomains_regex'], SOURCE_NEWSPAPERS)
TECH_NEWSPAPERS = filter(lambda x: 'tech' in x['allowed_subdomains_regex'], SOURCE_NEWSPAPERS)
CULTURE_NEWSPAPERS = filter(lambda x: 'culture' in x['allowed_subdomains_regex'], SOURCE_NEWSPAPERS)

TOPIC_TO_SOURCES = {
    'politics': POLITICS_NEWSPAPERS,
    'economy': ECONOMY_NEWSPAPERS,
    'sports': SPORTS_NEWSPAPERS,
    'tech': TECH_NEWSPAPERS,
    'culture': CULTURE_NEWSPAPERS
}
