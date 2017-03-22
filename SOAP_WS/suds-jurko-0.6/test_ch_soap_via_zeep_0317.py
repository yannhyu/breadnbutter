# test_ch_soap_via_zeep_0317.py

from zeep import Client
from zeep import xsd
from zeep.wsse.username import UsernameToken

WSDL_URL = 'https://ra.emdeon.com/astwebservice/aws.asmx?wsdl'
username = 'TPMEDLYTT'
password = 'c6EW9b-drM'

header = xsd.Element(
    '{https://ra.emdeon.com/AstWebService}auth',
    xsd.ComplexType([
        xsd.Element(
            '{https://ra.emdeon.com/AstWebService}username',
            xsd.String()),
        xsd.Element(
            '{https://ra.emdeon.com/AstWebService}password',
            xsd.String()),        
    ])
)

client = Client(wsdl=WSDL_URL, wsse=UsernameToken(username, password))

the_whole_thing = client.wsdl.dump()
print(the_whole_thing)

req_msg = 'Hello|CH|RT|WS'
doc = client.service.RunTransaction(username, password, req_msg)
print(doc)
#print(etree.tostring(doc, pretty_print=True))