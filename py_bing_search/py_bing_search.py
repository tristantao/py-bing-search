import requests, requests.utils
import time

class PyBingException(Exception):
    pass

class PyBingSearch(object):
    """
    Shell class for the individual searches
    """
    def __init__(self, api_key, query, query_base, safe=False):
        self.api_key = api_key
        self.safe = safe
        self.current_offset = 0
        self.query = query
        self.QUERY_URL = query_base

    def search(self, limit=50, format='json'):
        ''' Returns the result list, and also the uri for next page (returned_list, next_uri) '''
        return self._search(limit, format)

    def search_all(self, limit=50, format='json'):
        ''' Returns a single list containing up to 'limit' Result objects'''
        desired_limit = limit
        results = self._search(limit, format)
        limit = limit - len(results)
        while len(results) < desired_limit:
            more_results = self._search(limit, format)
            if not more_results:
                break
            results += more_results
            limit = limit - len(more_results)
            time.sleep(1)
        return results

##
##
## Web Search
##
##

class PyBingWebException(Exception):
    pass

class PyBingWebSearch(PyBingSearch):

    SEARCH_WEB_BASE = 'https://api.datamarket.azure.com/Bing/Search/Web'
    WEB_ONLY_BASE = 'https://api.datamarket.azure.com/Bing/SearchWeb/v1/Web'
    QUERYSTRING_TEMPLATE = '?Query={}&$top={}&$skip={}&$format={}'

    def __init__(self, api_key, query, web_only=False, safe=False):
        if web_only:
            query_base = self.WEB_ONLY_BASE + self.QUERYSTRING_TEMPLATE
        else:
            query_base = self.SEARCH_WEB_BASE + self.QUERYSTRING_TEMPLATE
        PyBingSearch.__init__(self, api_key, query, query_base, safe=safe)

    def _search(self, limit, format):
        '''
        Returns a list of result objects, with the url for the next page bing search url.
        '''
        url = self.QUERY_URL.format(requests.utils.quote("'{}'".format(self.query)), min(50, limit), self.current_offset, format)
        r = requests.get(url, auth=("", self.api_key))
        try:
            json_results = r.json()
        except ValueError as vE:
            if not self.safe:
                raise PyBingWebException("Request returned with code %s, error msg: %s" % (r.status_code, r.text))
            else:
                print ("[ERROR] Request returned with code %s, error msg: %s. \nContinuing in 5 seconds." % (r.status_code, r.text))
                time.sleep(5)
        packaged_results = [WebResult(single_result_json) for single_result_json in json_results['d']['results']]
        self.current_offset += min(50, limit, len(packaged_results))
        return packaged_results

class WebResult(object):
    '''
    The class represents a SINGLE search result.
    Each result will come with the following:

    #For the actual results#
    title: title of the result
    url: the url of the result
    description: description for the result
    id: bing id for the page

    #Meta info#:
    meta.uri: the search uri for bing
    meta.type: for the most part WebResult
    '''

    class _Meta(object):
        '''
        Holds the meta info for the result.
        '''
        def __init__(self, meta):
            self.type = meta['type']
            self.uri = meta['uri']

    def __init__(self, result):
        self.url = result['Url']
        self.title = result['Title']
        self.description = result['Description']
        self.id = result['ID']

        self.meta = self._Meta(result['__metadata'])

##
##
## Image Search
##
##

class PyBingImageException(Exception):
    pass

class PyBingImageSearch(PyBingSearch):

    IMAGE_QUERY_BASE = 'https://api.datamarket.azure.com/Bing/Search/Image' \
                 + '?Query={}&$top={}&$skip={}&$format={}'

    def __init__(self, api_key, query, safe=False):
        PyBingSearch.__init__(self, api_key, query, self.IMAGE_QUERY_BASE, safe=safe)

    def _search(self, limit, format):
        '''
        Returns a list of result objects, with the url for the next page bing search url.
        '''
        url = self.QUERY_URL.format(requests.utils.quote("'{}'".format(self.query)), min(50, limit), self.current_offset, format)
        r = requests.get(url, auth=("", self.api_key))
        try:
            json_results = r.json()
        except ValueError as vE:
            if not self.safe:
                raise PyBingImageException("Request returned with code %s, error msg: %s" % (r.status_code, r.text))
            else:
                print ("[ERROR] Request returned with code %s, error msg: %s. \nContinuing in 5 seconds." % (r.status_code, r.text))
                time.sleep(5)
        packaged_results = [ImageResult(single_result_json) for single_result_json in json_results['d']['results']]
        self.current_offset += min(50, limit, len(packaged_results))
        return packaged_results

class ImageResult(object):
    '''
    The class represents a single image search result.
    Each result will come with the following:

    #For the actual image results#
    self.id: id of the result
    self.title: title of the resulting image
    self.media_url: url to the full size image
    self.source_url: url of the website that contains the source image
    self.width: width of the image
    self.height: height of the image
    self.file_size: size of the image (in bytes) if available
    self.content_type the MIME type of the image if available
    self.meta: meta info

    #Meta info#:
    meta.uri: the search uri for bing
    meta.type: for the most part ImageResult
    '''

    class _Meta(object):
        '''
        Holds the meta info for the result.
        '''
        def __init__(self, meta):
            self.type = meta['type']
            self.uri = meta['uri']

    def __init__(self, result):

        self.id = result['ID']
        self.title = result['Title']
        self.media_url = result['MediaUrl']
        self.source_url = result['SourceUrl']
        self.display_url = result['DisplayUrl']
        self.width = result['Width']
        self.height = result['Height']
        self.file_size = result['FileSize']
        self.content_type = result['ContentType']
        self.meta = self._Meta(result['__metadata'])

##
##
## Video Search
##
##

class PyBingVideoException(Exception):
    pass

class PyBingVideoSearch(PyBingSearch):

    VIDEO_QUERY_BASE = 'https://api.datamarket.azure.com/Bing/Search/Video' \
                 + '?Query={}&$top={}&$skip={}&$format={}'

    def __init__(self, api_key, query, safe=False):
        PyBingSearch.__init__(self, api_key, query, self.VIDEO_QUERY_BASE, safe=safe)

    def _search(self, limit, format):
        '''
        Returns a list of result objects, with the url for the next page bing search url.
        '''
        url = self.QUERY_URL.format(requests.utils.quote("'{}'".format(self.query)), min(50, limit), self.current_offset, format)
        r = requests.get(url, auth=("", self.api_key))
        try:
            json_results = r.json()
        except ValueError as vE:
            if not self.safe:
                raise PyBingVideoException("Request returned with code %s, error msg: %s" % (r.status_code, r.text))
            else:
                print ("[ERROR] Request returned with code %s, error msg: %s. \nContinuing in 5 seconds." % (r.status_code, r.text))
                time.sleep(5)
        packaged_results = [VideoResult(single_result_json) for single_result_json in json_results['d']['results']]
        self.current_offset += min(50, limit, len(packaged_results))
        return packaged_results

class VideoResult(object):
    '''
    The class represents a single Video search result.
    Each result will come with the following:

    #For the actual Video results#
    self.id: id of the result
    self.title: title of the resulting Video
    self.media_url: url to the full size Video
    self.display_url: url to display on the search result.
    self.run_time: run time of the video
    self.meta: meta info

    #Meta info#:
    meta.uri: the search uri for bing
    meta.type: for the most part VideoResult
    '''

    class _Meta(object):
        '''
        Holds the meta info for the result.
        '''
        def __init__(self, meta):
            self.type = meta['type']
            self.uri = meta['uri']

    def __init__(self, result):

        self.id = result['ID']
        self.title = result['Title']
        self.media_url = result['MediaUrl']
        self.display_url = result['DisplayUrl']
        self.run_time = result['RunTime']
        self.meta = self._Meta(result['__metadata'])

##
##
## News Search
##
##

class PyBingNewsException(Exception):
    pass

class PyBingNewsSearch(PyBingSearch):

    NEWS_QUERY_BASE = 'https://api.datamarket.azure.com/Bing/Search/News' \
                 + '?Query={}&$top={}&$skip={}&$format={}'

    def __init__(self, api_key, query, safe=False):
        PyBingSearch.__init__(self, api_key, query, self.NEWS_QUERY_BASE, safe=safe)

    def _search(self, limit, format):
        '''
        Returns a list of result objects, with the url for the next page bing search url.
        '''
        url = self.QUERY_URL.format(requests.utils.quote("'{}'".format(self.query)), min(50, limit), self.current_offset, format)
        r = requests.get(url, auth=("", self.api_key))
        try:
            json_results = r.json()
        except ValueError as vE:
            if not self.safe:
                raise PyBingNewsException("Request returned with code %s, error msg: %s" % (r.status_code, r.text))
            else:
                print ("[ERROR] Request returned with code %s, error msg: %s. \nContinuing in 5 seconds." % (r.status_code, r.text))
                time.sleep(5)
        packaged_results = [NewsResult(single_result_json) for single_result_json in json_results['d']['results']]
        self.current_offset += min(50, limit, len(packaged_results))
        return packaged_results

class NewsResult(object):
    '''
    The class represents a single News search result.
    Each result will come with the following:

    #For the actual News results#
    self.id: id of the result
    self.title: title of the resulting News
    self.url: url to the News
    self.description: description of the article
    self.date: date of the News
    self.meta: meta info

    #Meta info#:
    meta.uri: the search uri for bing
    meta.type: for the most part NewsResult
    '''

    class _Meta(object):
        '''
        Holds the meta info for the result.
        '''
        def __init__(self, meta):
            self.type = meta['type']
            self.uri = meta['uri']

    def __init__(self, result):
        self.id = result['ID']
        self.title = result['Title']
        self.url = result['Url']
        self.source = result['Source']
        self.description = result['Description']
        self.date = result['Date']
        self.meta = self._Meta(result['__metadata'])
