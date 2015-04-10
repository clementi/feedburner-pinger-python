from enum import Enum
import json
import requests


Status = Enum('Status', 'SUCCEEDED THROTTLED FAILED')


class PingResponse(object):
    def __init__(self, response):
        self.message = response['message']
        self.status = self._get_status(response['status'])

    def _get_status(self, status):
        if status == 'SUCCEEDED':
            return Status.SUCCEEDED
        elif status == 'THROTTLED':
            return Status.THROTTLED
        else:
            return Status.FAILED


def ping(url):
    fields = {'url': url}
    resp = requests.post('http://feedburner-pinger.herokuapp.com', data=fields)
    response_dict = json.loads(resp.text)
    return PingResponse(response_dict)
