import json
from bson import json_util

def send_json(json_object):
    return json.loads(json_util.dumps(json_object))

def check_body(b):
    body = {}
    if (b) and (isinstance(b, dict)) and (len(b) != 0):
        body = b
    return body