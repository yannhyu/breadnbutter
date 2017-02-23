# ebureau_real_time.py
# -*- coding: utf-8 -*-

import requests
import time
import random
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

EB_REAL_TIME_URL = "https://factory.ebureau.com/test/"

def generate_xml_request(login_data, tranx_data):
    results = []
    results.append('<root>\n')
    results.append('  <login>\n')
    results.append('    <userid>{}</userid>\n'.format(login_data.get('userid')))
    results.append('    <password>{}</password>\n'.format(login_data.get('password')))
    results.append('    <realtime>1</realtime>\n')
    results.append('    <protocol>1</protocol>\n')
    results.append('    <timeout>10</timeout>\n')
    results.append('    <sid>{}</sid>\n'.format(login_data.get('sid')))
    results.append('    <output>account</output>\n')
    results.append('  </login>\n')
    results.append('  <transaction>\n')
    results.append('    <input>\n')
    results.append('      <account>\n')
    results.append('        <subuserid>{}</subuserid>\n'.format(tranx_data.get('subuserid')))
    results.append('        <sourceid>{}</sourceid>\n'.format(tranx_data.get('sourceid')))
    results.append('        <groupid>{}</groupid>\n'.format(tranx_data.get('groupid')))
    results.append('        <account>{}</account>\n'.format(tranx_data.get('account')))   
    results.append('      </account>\n')
    results.append('      <data>\n')
    results.append('        <first>{}</first>\n'.format(tranx_data.get('first')))
    results.append('        <last>{}</last>\n'.format(tranx_data.get('last'))) 
    results.append('        <address>{}</address>\n'.format(tranx_data.get('address')))
    results.append('        <city>{}</city>\n'.format(tranx_data.get('city')))
    results.append('        <state>{}</state>\n'.format(tranx_data.get('state')))
    results.append('        <zip>{}</zip>\n'.format(tranx_data.get('zip')))
    results.append('        <phone>{}</phone>\n'.format(tranx_data.get('phone')))
    results.append('        <social>{}</social>\n'.format(tranx_data.get('social')))
    results.append('        <dob>{}</dob>\n'.format(tranx_data.get('dob')))
    results.append('        <email>{}</email>\n'.format(tranx_data.get('email')))#
    results.append('      </data>\n')
    results.append('    </input>\n')    
    results.append('  </transaction>\n')
    results.append('</root>')
    return ''.join(results)

def call_ebureau_real_time(xml_req):
    headers = {'Content-Type': 'application/xml'} # set what your server accepts
    time.sleep(random.uniform(1.2, 1.5))
    results = requests.post(EB_REAL_TIME_URL, data=xml_req, headers=headers)

    return results.text

def request2ebureau_real_time(data):
    LOGIN_DATA = {    
                'userid': 'medly00003', 
                'password': 'cp96ah11wg18',
                'sid': 'xtech:locate:consumer:4'
            }

    xml_req = generate_xml_request(LOGIN_DATA, data)
    print('++++++++++++ Request +++++++++++++')
    print(xml_req)
    print('++++++++++++++++++++++++++++++++++')
    headers = {'Content-Type': 'application/xml'} # set what your server accepts
    time.sleep(random.uniform(1.2, 1.5))
    results = requests.post(EB_REAL_TIME_URL, data=xml_req, headers=headers)

    return results.text

def parse_xml(xml_str):
    tree = ET.ElementTree(ET.fromstring(xml_str))
    root = tree.getroot()
    #for child in root:
    #    print(child.tag)
    #for elem in tree.iter():
    #    print(elem.tag)
    for elem in tree.iterfind('transaction/input/account'):
        print(elem.tag)


if __name__ == '__main__':    
    ACCT_DATA = {
                'subuserid': '012345',
                'sourceid': 'source',
                'groupid': 'use cust_id here',
                'account': 'use seqnum here',
                'first': 'John',
                'last': 'Smith',
                'address': '123 main st',
                'city': 'Plymouth',
                'state': 'MN',
                'zip': '54312',
                'phone': '9875517824',
                'social': '111223333',
                'dob': '19640101',
                'email': 'johnsmith@domain.com'
            }
    parse_xml(request2ebureau_real_time(ACCT_DATA))