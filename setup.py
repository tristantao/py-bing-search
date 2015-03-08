from setuptools import setup, find_packages
import os
import platform

DESCRIPTION = "A simple python wrapper for the Azure Bing Search API."

LONG_DESCRIPTION = None
try:
    LONG_DESCRIPTION = open('README.md').read()
except:
    pass

CLASSIFIERS = [
    'Development Status :: 0.1.0 - Beta',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Software Development :: Libraries :: Python Modules',
]

setup(
    name='pybingsearch',
    version='0.1.0',
    author=u'tristan tao',
    author_email='tristan@teamleada.com',
    py_modules=['py-bing-search'],
    url='http://github.com/tristantao/py-bing-search',
    license='MIT',
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    platforms=['any'],
    classifiers=CLASSIFIERS,
    install_requires=['requests'],
)
