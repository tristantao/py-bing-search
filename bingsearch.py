import urllib2
import requests
import pdb


class BingSearch(object):

    #QUERY_URL = 'https://api.datamarket.azure.com/Bing/Search/v1/Composite' \
    #             + '?Sources={}&Query={}&$top={}&$skip={}&$format={}'
    QUERY_URL = 'https://api.datamarket.azure.com/Bing/SearchWeb/v1/Composite' \
                 + '?Sources={}&Query={}&$top={}&$skip={}&$format={}'


    def __init__(self, api_key):
        self.api_key = api_key

    def search(self, query, limit=50, offset=0, format='json'):
        return self._search(query, limit, offset, format)

    def search_all(self, query, limit=50, format='json'):
        results = self._search(query, limit, 0, format)
        while results.total > len(results) and len(results) < limit:
            max = limit - len(results)
            more_results = self._search(query, max, len(results), format)
            results += more_results
        return results

    def _search(self, query, limit, offset, format):
        url = self.QUERY_URL.format(urllib2.quote("'web'"),
                                    urllib2.quote("'{}'".format(query)),
                                    limit, offset, format)
        print "poop"
        print self.api_key
        #url = "https://api.datamarket.azure.com/Bing/SearchWeb/v1/Web?Query=%27apple%27"
        url = "https://api.datamarket.azure.com/Bing/SearchWeb/v1/Web?Query=%27apple%20iphone%27&$format=json"
        print url
        r = requests.get(url, auth=("", self.api_key))
        print r
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
        pdb.set_trace()
        self.results = []
        for result in result['Web']:
            self.results.append(self._Result(result))

    def __len__(self):
        return len(self.results)

    def __iadd__(self, results):
        self.results.extend(results.results)
        return self
