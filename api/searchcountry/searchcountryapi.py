import json
from nzme_skynet.core.api.apiconnection import ApiConnection


class JsonPayload(object):
    def __init__(self, j):
        self.__dict__ = json.loads(j)


class SearchCountryApi(object):
    api_url = 'country/get/iso2code/NZ'
    base_url = 'services.groupkt.com/'

    def get(self):
        return ApiConnection(host_url=self.base_url).get(uri=self.api_url)

    @staticmethod
    def convert_payload_to_json(payload):
        return JsonPayload(payload)

