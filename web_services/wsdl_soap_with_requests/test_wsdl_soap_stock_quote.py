# test_wsdl_soap_stock_quote.py
import time
import xml
import requests
from contextlib import closing
from jinja2 import Environment, PackageLoader

WSDL_URL = 'http://www.webservicex.net/stockquote.asmx?WSDL'

def generate_req_body(req_data):
    env = Environment(loader=PackageLoader('ch', 'templates'))
    template = env.get_template('soaprequests/StockQuoteSericeRequest.xml')
    body = template.render(Data=req_data)
    #print(body)
    return body

def get_req_headers():
    headers = {'Content-Type': 'text/xml; charset=UTF-8'}
    #print(headers)
    return headers

def get_reqs():
    return ['MSFT', 'GOOG', 'AA']


if __name__ == '__main__':
    start_time = time.time()
    #auth = (username, password)
    auth=None
    ses = requests.session()
    #ses.config['keep_alive'] = False
    ses.keep_alive = False
    for req_data in get_reqs():
        headers = get_req_headers()
        response = ses.post(WSDL_URL,data=req_data,headers=headers,verify=True,timeout=30,auth=auth,stream=False)
        resp_payload = response.content
        print(resp_payload)
        #try:
        #    ch_rt_payload = xmltodict.parse(resp_payload)
        #    ch_rt_tx_res_ec = ch_rt_payload['soap:Envelope']['soap:Body']['RunTransactionResponse']['RunTransactionResult']
        #except xml.parsers.expat.ExpatError as e:
        #    print('Error digesting response due to {}'.format(e))
        #else:
        #    ch_rt_tx_res = b64decode(ch_rt_tx_res_ec)
        #    print(ch_rt_tx_res)

    print("--- {} seconds ---".format(time.time() - start_time)) 
