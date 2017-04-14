# ch_rt_with_template_session_1.py

import time
import xml
import requests
from contextlib import closing
import xmltodict
from base64 import b64decode, b64encode
from jinja2 import Environment, PackageLoader

WSDL_URL = 'https://ra.emdeon.com/astwebservice/aws.asmx?wsdl'
username = 'TPMEDLYTT'
password = 'c6EW9b-drM'

def generate_req_body(req_data):
    env = Environment(loader=PackageLoader('ch', 'templates'))
    template = env.get_template('soaprequests/CHRealtimeSericeRequest.xml')
    body = template.render(UserName=username, Password=password, Data=req_data)
    #print(body)
    return body

def get_req_headers_with_auth():
    auth = b64encode('{}:{}'.format(username, password)).replace('\n', '')
    #print(auth)
    headers = {'Content-Type': 'text/xml; charset=UTF-8', 'Authorization': 'Basic {}'.format(auth)}
    #print(headers)
    return headers

def get_req_headers():
    headers = {'Content-Type': 'text/xml; charset=UTF-8'}
    #print(headers)
    return headers    

def get_reqs():
    result = []
    req_tests = """
        BCGAC|1538144910|C-N-000004-608107640680|3/21/2016|3/21/2016|CHERRITA||HILL|8/25/1971|F|240131605|GASTONIA|NC|28052|0|5126|574591|TPREVFNDR|YPP240131605|031017_000004_002017
        BCGAC|1538144910|C-N-000004-609507624210|4/4/2016|4/4/2016|ELLIS||ATKINS|1/9/1965|M|237330965|STATESVILLE|NC|28677|0|5126|574591|TPREVFNDR|YPP237330965|031017_000004_002017
        BCGAC|1538144910|C-N-000004-6195G810044A|7/13/2016|7/13/2016|JENNIFER||DIGIACOMO|9/21/1984|F|144905188|KNIGHTDALE|NC|27545|0|5126|574591|TPREVFNDR|YPP144905188|031017_000004_002017
        BCGAC|1538144910|C-N-000004-620945502860|7/27/2016|7/27/2016|RHONDA||HUNT|12/17/1962|F|238338978|DENTON|NC|27239|0|5126|574591|TPREVFNDR|YPP238338978|031017_000004_002017
        BCGAC|1538144910|C-N-000004-626507601800|9/21/2016|9/21/2016|PAMELA||FULBRIGHT|2/5/1960|F|245172606|CRAMERTON|NC|28032|0|5126|574591|TPREVFNDR|YPP245172606|031017_000004_002017
        BCGAC|1538144910|C-N-000004-635707622210|12/22/2016|12/22/2016|ELZIE||GOODE|7/26/1988|M|247757729|CONCORD|NC|28025|0|5126|574591|TPREVFNDR|YPP247757729|031017_000004_002017
        BCGAC|1538144910|C-N-000004-635707628440|12/22/2016|12/22/2016|ELZIE||GOODE|7/26/1988|M|247757729|CONCORD|NC|28025|0|5126|574591|TPREVFNDR|YPP247757729|031017_000004_002017
        """
    req_tests = req_tests.strip()
    tmp_list = req_tests.split('\n')
    result = [item.strip() for item in tmp_list]
    #print(result)
    return result    

if __name__ == '__main__':
    start_time = time.time()
    auth = (username, password)
    req_msgs = get_reqs()
    ses = requests.session()
    #ses.config['keep_alive'] = False
    ses.keep_alive = False
    for req_data in req_msgs[:3]:
        req_data_ec = b64encode(req_data)
        body = generate_req_body(req_data_ec)
        headers = get_req_headers()
        response = ses.post(WSDL_URL,data=body,headers=headers,verify=True,timeout=30,auth=auth,stream=False)
        #response = ses.post(WSDL_URL,data=body,headers=headers,verify=True,timeout=30,stream=False)
        resp_payload = response.content
        #print(resp_payload)
        try:
            ch_rt_payload = xmltodict.parse(resp_payload)
            ch_rt_tx_res_ec = ch_rt_payload['soap:Envelope']['soap:Body']['RunTransactionResponse']['RunTransactionResult']
        except xml.parsers.expat.ExpatError as e:
            print('Error digesting response due to {}'.format(e))
        else:
            ch_rt_tx_res = b64decode(ch_rt_tx_res_ec)
            print(ch_rt_tx_res)

    print("--- {} seconds ---".format(time.time() - start_time))        

