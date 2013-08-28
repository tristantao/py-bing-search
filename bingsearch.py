import urllib2
import requests


class BingSearch(object):

    QUERY_URL = 'https://api.datamarket.azure.com/Bing/Search/v1/Composite' \
                 + '?Sources={}&Query={}&$top={}&$format={}'

    def __init__(self, api_key):
        self.api_key = api_key

    def search(self, query, limit=50, format='json'):
        url = self.QUERY_URL.format(urllib2.quote("'web'"),
                                    urllib2.quote("'{}'".format(query)),
                                    limit, format)
        r = requests.get(url, auth=('', self.api_key))
        return Result(r.json()['d']['results'])

class Result(object):

    class _Meta(object):
        def __init__(self, meta):
            self.type = meta['type']
            self.uri = meta['uri']

    class _Result(object):
        def __init__(self, result):
            self.url = result['Url']
            self.title = result['Title']
            self.description = result['Description']
            self.meta = Result._Meta(result['__metadata'])

    def __init__(self, results):
        result = results[0]
        self.meta = self._Meta(result['__metadata'])
        self.total = result['WebTotal']
        self.results = []
        for result in result['Web']:
            self.results.append(self._Result(result))
