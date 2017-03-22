# test_ch_soap_0317.py

from base64 import b64decode, b64encode
import logging
from suds.client import Client
from suds.plugin import MessagePlugin
from suds.wsse import *
from datetime import timedelta,date,datetime,tzinfo
import requests
from requests.auth import HTTPBasicAuth
import suds_requests

logging.basicConfig(level=logging.INFO) 
logging.getLogger('suds.client').setLevel(logging.DEBUG) 
logging.getLogger('suds.transport').setLevel(logging.DEBUG)

class HeaderPlugin(MessagePlugin):
    def __init__(self):
        self.document = None

    def parsed(self, context):
        self.document = context.reply

    def get_headers(self, method):
        method = method.method
        binding = method.binding.output
        rtypes = binding.headpart_types(method, False)

        envns = ('SOAP-ENV', 'http://schemas.xmlsoap.org/soap/envelope/')
        soapenv = self.document.getChild('Envelope', envns)
        soapheaders = soapenv.getChild('Header', envns)
        nodes = soapheaders.children
        if len(nodes):
            resolved = rtypes[0].resolve(nobuiltin=True)
            return binding.unmarshaller().process(nodes[0], resolved)
        return None


def addSecurityHeader(client,username,password):
    security=Security()
    userNameToken=UsernameToken(username,password)
    timeStampToken=Timestamp(validity=600)
    security.tokens.append(userNameToken)
    security.tokens.append(timeStampToken)
    client.set_options(wsse=security)


if __name__ == '__main__':
    WSDL_URL = 'https://ra.emdeon.com/astwebservice/aws.asmx?wsdl'
    #WSDL_URL = 'https://ra.emdeon.com/astwebservice/aws.asmx'
    #Session request and authentication:
    username = 'TPMEDLYTT'
    password = 'c6EW9b-drM'
    session = requests.session()
    session.auth = (username, password)

    hp = HeaderPlugin()
    client = Client(WSDL_URL, faults=False, cachingpolicy=1, location=WSDL_URL, transport=suds_requests.RequestsTransport(session))
    #client = Client(WSDL_URL, username='TPMEDLYTT', password='c6EW9b-drM', plugins=[hp])
    list_of_methods = [method for method in client.wsdl.services[0].ports[0].methods]

    print(list_of_methods)

    method = client.wsdl.services[0].ports[0].methods["RunTransaction"]
    params = method.binding.input.param_defs(method)
    print(params)

    addSecurityHeader(client, username, password)
    #req_msg = b64encode('Hello|CH|RT|WS')
    req_msg = b64encode(
    """
    BCGAC|1538144910|C-N-000004-635707628440|2016-12-22 00:00:00|2016-12-22 00:00:00|ELZIE|None|GOODE|1988-07-26 00:00:00|M|247757729|CONCORD|NC|28025|0|5126|574591|TPREVFNDR|YPP247757729|031017_000004_002017
    """)
    result = client.service.RunTransaction(UserName=username, Password=password, Request=req_msg)
    print(result)
    status, data = result
    print(b64decode(data))

    #headers = hp.get_headers(result)
    #print(headers)