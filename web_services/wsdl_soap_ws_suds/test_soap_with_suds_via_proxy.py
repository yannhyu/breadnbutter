# test_soap_with_suds_via_proxy.py

import logging
from suds.client import Client
from suds.wsse import *
from datetime import timedelta,date,datetime,tzinfo
#import requests
#from requests.auth import HTTPBasicAuth
from suds.transport.https import HttpAuthenticated
#import suds_requests

logging.basicConfig(level=logging.INFO) 
logging.getLogger('suds.client').setLevel(logging.DEBUG) 
logging.getLogger('suds.transport').setLevel(logging.DEBUG)

#Session request and authentication:
#username=input('Username:')
#password=input('password:')
#session = requests.session()
#session.auth=(username, password)

WSDL_URL = 'http://www.webservicex.net/stockquote.asmx?WSDL'
#client = Client(WSDL_URL, faults=False, cachingpolicy=1, location=WSDL_URL, transport=suds_requests.RequestsTransport(session))
HttpsProxy = 'https://fwdproxy.medlytix.org:8080'
HttpProxy = 'http://fwdproxy.medlytix.org:8080'
proxies = {
  "https": HttpsProxy,
  "http": HttpProxy
}
credentials = dict(username='...', password='...', proxy=proxies)
trans = HttpAuthenticated(**credentials)
client = Client(WSDL_URL, faults=False, cachingpolicy=1, location=WSDL_URL, transport=trans)

#Consume the relevant method (or operation) :
#result=client.service.methodName(Inputs)
symbol = 'GOOG'
result=client.service.GetQuote(symbol=symbol)

print(result)

