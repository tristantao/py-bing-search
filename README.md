Extremely thin python wrapper for Microsoft Azure Bing Search API. Please note that this module does not use the Bing Search API 2.0 AppIDs which will be deprecated on August 1, 2012. This module requires that you sign up to the Windows Azure Marketplace and apply for an application key.

The modules uses OAuth, so you'll need to get your key here (free for up to 5K/Mon):
* [All Purpose](https://datamarket.azure.com/dataset/5BA839F1-12CE-4CCE-BF57-A49D98D29A44)
* [Web Search Only](https://datamarket.azure.com/dataset/8818F55E-2FE5-4CE3-A617-0B8BA8419F65)


Installation
=====

```pip install py-bing-search```

*Requires the requests library.

Usage
=====

Remember to set the `API_KEY` as your own.

    >>> from py_bing_search import PyBingSearch
    >>> bing = PyBingSearch('Your-Api-Key-Here')
    >>> result_list, next_uri = bing.search("Python Software Foundation", limit=50, format='json')

You can also run search_all to keep search going until it fills your required quota
    >>> result_list = bing.search_all("Python Software Foundation", limit=130, format='json')
    >>> len(result_list) == 130
    True
    >>>

result_list is a list of search results. next_uri is the search link to the next page

    >>> result_list[0].description
    u'Python Software Foundation Home Page. The mission of the Python Software Foundation is to promote, protect, and advance the Python programming language, and to ...'
    
    >>> for result in result_list:
    ...     print result.url
    ...
    u'http://www.python.org/psf/
    ...

What you get is a list of Result() instances, each comes with the following values:
    
```py
self.title:         title of the result
self.url:           the url of the result
self.description:   description for the result
self.id:            bing id for the page

#Meta info:
self.meta.uri:      the search uri for bing
self.meta.type:     for the most part WebResult
```
    
