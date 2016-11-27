COUCHBASE_HOSTS = [
# CLOUD NODES
    'couchbase-worker-service'
]
COUCHBASE_PORT = 8091
COUCHBASE_BUCKET = 'default'
COUCHBASE_CONNECTION_STRING = 'http://{hosts}/{bucket}'.format(hosts=','.join(['%s:%s' % (host, COUCHBASE_PORT) for host in COUCHBASE_HOSTS]),  
                                                               bucket=COUCHBASE_BUCKET)
COUCHBASE_USERNAME = 'Administrator'
COUCHBASE_PASSWORD = 'password'
