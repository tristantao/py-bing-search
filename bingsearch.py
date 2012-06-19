import requests

URL = 'https://api.datamarket.azure.com/Data.ashx/Bing/SearchWeb/Web?Query=%(query)s&$top=50&$format=json'
API_KEY = 'SECRET_API_KEY'

def request(query, **params):
    r = requests.get(URL % {'query': query}, auth=('', API_KEY))
    return r.json['d']['results']
