# test_soap_wsdl.py

import logging
from suds.client import Client
from suds.wsse import *
from datetime import timedelta,date,datetime,tzinfo
import requests
from requests.auth import HTTPBasicAuth
import suds_requests

logging.basicConfig(level=logging.INFO) 
logging.getLogger('suds.client').setLevel(logging.DEBUG) 
logging.getLogger('suds.transport').setLevel(logging.DEBUG)

#Session request and authentication:
#username=input('Username:')
#password=input('password:')
session = requests.session()
#session.auth=(username, password)

WSDL_URL = 'http://www.webservicex.net/stockquote.asmx?WSDL'
client = Client(WSDL_URL, faults=False, cachingpolicy=1, location=WSDL_URL, transport=suds_requests.RequestsTransport(session))

#Consume the relevant method (or operation) :
#result=client.service.methodName(Inputs)
symbol = 'GOOG'
result=client.service.GetQuote(symbol=symbol)

print(result)