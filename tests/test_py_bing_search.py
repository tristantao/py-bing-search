from unittest import TestCase
import time, ConfigParser
import os

from py_bing_search import PyBingWebSearch
from py_bing_search import PyBingImageSearch
from py_bing_search import PyBingVideoSearch
from py_bing_search import PyBingNewsSearch

def grab_secret():
    config = ConfigParser.ConfigParser()
    config.readfp(open('tests/secrets.cfg'))
    return config.get('secret', 'secret')

def setUpModule():
    'called once, before anything else in this module'
    global SECRET_KEY
    SECRET_KEY = grab_secret()
    print('Setting Up Test')

class TestPyBingWebSearch(TestCase):

    def tearDown(self):
        '''To not overload API calls'''
        time.sleep(0.75)

    def test_can_search(self):
        web_bing = PyBingWebSearch(SECRET_KEY, "Python Software Foundation")
        result_one = web_bing.search(limit=50)
        self.assertTrue(len(result_one) == 50)
        self.assertTrue("Python" in result_one[0].title)
        time.sleep

    def test_search_all(self):
        web_bing = PyBingWebSearch(SECRET_KEY, "Python Software Foundation")
        result_one = web_bing.search_all(limit=60)
        self.assertTrue(len(result_one) == 60)
        self.assertTrue("Python" in result_one[0].title)

# Image Tests
class TestPyBingImageSearch(TestCase):

    def tearDown(self):
        '''To not overload API calls'''
        time.sleep(0.75)

    def test_can_search(self):
        web_bing = PyBingImageSearch(SECRET_KEY, "Python Software Foundation")
        result_one = web_bing.search(limit=50)
        self.assertTrue(len(result_one) == 50)
        self.assertTrue("Python" in result_one[0].title)

    def test_search_all(self):
        web_bing = PyBingImageSearch(SECRET_KEY, "Python Software Foundation")
        result_one = web_bing.search_all(limit=60)
        self.assertTrue(len(result_one) == 60)
        self.assertTrue("Python" in result_one[0].title)

# Video Tests
class TestPyBingVideoSearch(TestCase):

    def tearDown(self):
        '''To not overload API calls'''
        time.sleep(0.75)

    def test_can_search(self):
        web_bing = PyBingVideoSearch(SECRET_KEY, "Python Software Foundation")
        result_one = web_bing.search(limit=50)
        self.assertTrue(len(result_one) == 50)
        self.assertTrue("Python" in result_one[0].title)

    def test_search_all(self):
        web_bing = PyBingVideoSearch(SECRET_KEY, "Python Software Foundation")
        result_one = web_bing.search_all(limit=60)
        self.assertTrue(len(result_one) == 60)
        self.assertTrue("Python" in result_one[0].title)

# News Tests
class TestPyBingNewsSearch(TestCase):

    def tearDown(self):
        '''To not overload API calls'''
        time.sleep(0.75)

    def test_can_search(self):
        web_bing = PyBingNewsSearch(SECRET_KEY, "Python Software Foundation")
        result_one = web_bing.search(limit=50)
        self.assertTrue(len(result_one) > 0)
        self.assertTrue("Python" in result_one[0].title)

    def test_search_all(self):
        web_bing = PyBingNewsSearch(SECRET_KEY, "Python Software Foundation")
        result_one = web_bing.search_all(limit=60)
        self.assertTrue(len(result_one) == 60)
        self.assertTrue("Python" in result_one[0].title)
