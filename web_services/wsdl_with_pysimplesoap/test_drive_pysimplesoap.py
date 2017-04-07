# test_drive_pysimplesoap.py

#!/usr/bin/python
# -*- coding: utf-8 -*-
# ch_real_time_process.py
import os.path
import sys
from datetime import timedelta, date, datetime, tzinfo
import time
from base64 import b64decode, b64encode
import logging.config
import requests
from requests.auth import HTTPBasicAuth
import urllib2
from pysimplesoap.client import SoapClient

logging.config.dictConfig({
    'version': 1,
    'formatters': {
        'verbose': {
            'format': '%(name)s: %(message)s'
        }
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'pysimplesoap.helpers': {
            'level': 'DEBUG',
            'propagate': True,
            'handlers': ['console'],
        },
    }
})

HttpsProxy = 'https://fwdproxy.medlytix.org:8080'
HttpProxy = 'http://fwdproxy.medlytix.org:8080'
proxies = {
  "https": HttpsProxy,
  "http": HttpProxy
}
opener = urllib2.build_opener(
                urllib2.HTTPHandler(),
                urllib2.HTTPSHandler(),
                urllib2.ProxyHandler({'http': HttpProxy}))
urllib2.install_opener(opener)

username = 'someone'
password = 'nottelling'
auth = b64encode('%s:%s' % (username, password)).replace('\n', '')

WSDL_URL = 'http://www.webservicex.net/stockquote.asmx?WSDL'
client = SoapClient(wsdl=WSDL_URL,
                    sessions=True,
                    cache = None,
                    trace=True,
                    ns='web',
                    location=WSDL_URL,
                    http_headers={'Authorization': "Basic %s" % auth},
                    exceptions=True)
client['AuthHeaderElement'] = {'username': 'someone', 'password': 'nottelling'}
response = client.GetQuote(symbol='GOOG')
print('GetQuote: {}'.format(response['GetQuoteResult']))
