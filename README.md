Extremely thin python wrapper for Microsoft Azure Bing Search API.

Usage
=====

Just remember to set the `API_KEY` as your own.

    >>> import bingsearch
    >>> bingsearch.API_KEY='Your-Api-Key-Here'
    >>> r = bingsearch.request("Python Software Foundation")
    >>> r.status_code
    200
    >>> r[0]['Description']
    u'Python Software Foundation Home Page. The mission of the Python Software Foundation is to promote, protect, and advance the Python programming language, and to ...'
    >>> r[0]['Url']
    u'http://www.python.org/psf/

