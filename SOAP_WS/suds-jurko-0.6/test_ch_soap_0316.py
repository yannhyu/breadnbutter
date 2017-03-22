# test_ch_soap_0316.py

from base64 import b64decode, b64encode
from suds.client import Client
from suds.plugin import MessagePlugin

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

username='TPMEDLYTT'
password='c6EW9b-drM'

hp = HeaderPlugin()    
#client = Client('https://ra.emdeon.com/astwebservice/aws.asmx?wsdl', username='TPMEDLYTT', password='c6EW9b-drM', plugins=[hp])
client = Client('https://ra.emdeon.com/astwebservice/aws.asmx?wsdl', plugins=[hp])
list_of_methods = [method for method in client.wsdl.services[0].ports[0].methods]

print(list_of_methods)

method = client.wsdl.services[0].ports[0].methods["RunTransaction"]
params = method.binding.input.param_defs(method)
print(params)

req_msg = b64encode('Hello|CH|RT|WS')
result = client.service.RunTransaction(UserName=username, Password=password, Request=req_msg)
print(result)
print(b64decode(result))
#headers = hp.get_headers(result)
#print(headers)