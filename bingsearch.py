import urllib2
import requests

URL = 'https://api.datamarket.azure.com/Bing/Search/v1/Composite' \
      + '?Sources=%(source)s&Query=%(query)s&$top=50&$format=json'
API_KEY = 'SECRET_API_KEY'

def request(query, **params):
    url = URL % {'source': urllib2.quote("'web'"),
                 'query': urllib2.quote("'"+query+"'")}
    r = requests.get(url, auth=('', API_KEY))
    return r.json()['d']['results']
