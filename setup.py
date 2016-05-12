from setuptools import setup, find_packages
import os
import platform

DESCRIPTION = "A simple lightweight python wrapper for the Azure Bing Search API."
VERSION = '0.2.1'
LONG_DESCRIPTION = None
try:
    LONG_DESCRIPTION = open('README.md').read()
except:
    pass

CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Software Development :: Libraries :: Python Modules',
]

KEYWORDS = ['Azure', 'Bing', 'API', 'Search']

INSTALL_REQUIRES = [
    'requests',
]

setup(
    name='py-bing-search',
    packages = ['py_bing_search'],
    #py_modules=['py_bing_search'],
    version=VERSION,
    author=u'Tristan Tao',
    author_email='tristan@teamleada.com',
    url='https://github.com/tristantao/py-bing-search',
    license='MIT',
    keywords=KEYWORDS,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    classifiers=CLASSIFIERS,
    install_requires=INSTALL_REQUIRES,
)
