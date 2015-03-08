from setuptools import setup, find_packages
import os
import platform

DESCRIPTION = "A simple lightweight python wrapper for the Azure Bing Search API."
VERSION = '0.1.2'
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

INSTALL_REQUIRES = [
    'requests',
]

setup(
    name='py-bing-search',
    packges = ['py-bing-search'],
    version=VERSION,
    author=u'Tristan Tao',
    author_email='tristan@teamleada.com',
    py_modules=['py-bing-search'],
    url='https://github.com/tristantao/py-bing-search',
    download_url = 'https://github.com/tristantao/py-bing-search/tarball/0.1.2',
    license='MIT',
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    classifiers=CLASSIFIERS,
    install_requires=INSTALL_REQUIRES,
)
