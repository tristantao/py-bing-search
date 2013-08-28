Extremely thin python wrapper for Microsoft Azure Bing Search API. Please note that this module does not use the Bing Search API 2.0 AppIDs which will be deprecated on August 1, 2012. This module requires that you sign up to the Windows Azure Marketplace and apply for an application key.

Usage
=====

Just remember to set the `API_KEY` as your own.

    >>> from bingsearch import BingSearch
    >>> searcher = BingSearch('Your-Api-Key-Here')
    >>> r = searcher.search("Python Software Foundation", limit=50, format='json')
    >>> r.total
    50
    >>> r.results[0].description
    u'Python Software Foundation Home Page. The mission of the Python Software Foundation is to promote, protect, and advance the Python programming language, and to ...'
    >>> r.results[0].url
    u'http://www.python.org/psf/
