# step_1_test_soap.py

from SOAPpy import WSDL
wsdlFile = 'http://www.webservicex.net/stockquote.asmx?WSDL'
server = WSDL.Proxy(wsdlFile)
print(server.methods.keys())
callInfo = server.methods['GetQuote']

print(callInfo.inparams)
print(callInfo.inparams[0].name)
print(callInfo.inparams[0].type)

print(callInfo.outparams)
print(callInfo.outparams[0].name)
print(callInfo.outparams[0].type)

try:
    res = server.GetQuote('MSFT')
    print(res)
except Exception as ex:
    print(ex)