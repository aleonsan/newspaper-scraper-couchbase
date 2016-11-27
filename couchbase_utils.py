from couchbase.admin import Admin
from constants import COUCHBASE_USERNAME, COUCHBASE_PASSWORD, COUCHBASE_HOSTS


def get_bucket_stats(bucket_name='default'):
    admin = Admin(COUCHBASE_USERNAME, COUCHBASE_PASSWORD, COUCHBASE_HOSTS[0])
    return admin.bucket_info(bucket_name).value['basicStats']

def flush_bucket(bucket_name='default'):
    admin = Admin(COUCHBASE_USERNAME, COUCHBASE_PASSWORD, COUCHBASE_HOSTS[0])
    return admin.http_request('/pools/default/buckets/%s/controller/doFlush' % bucket_name, 'POST')
