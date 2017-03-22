# test_requests_via_proxy.py
import requests
from xml.dom import minidom
import sys

EB_REAL_TIME_URL = "https://factory.ebureau.com/test/"
#EB_REAL_TIME_HTTPSPROXY = "https://fwdproxy.medlytix.org:8080"
#EB_REAL_TIME_HTTPPROXY = "http://fwdproxy.medlytix.org:8080"
EB_REAL_TIME_HTTPSPROXY = "https://fwdproxy.medlytix.org:8081"
EB_REAL_TIME_HTTPPROXY = "http://fwdproxy.medlytix.org:8081"

xml_1 = """
<root>
  <login>
    <userid>medly00003</userid>
    <password>cp96ah11wg18</password>
    <realtime>1</realtime>
    <protocol>1</protocol>
    <timeout>10</timeout>
    <sid>xtech:locate:consumer:4</sid>
    <output>account</output>
  </login>
  <transaction>
    <input>
      <account>
        <subuserid>Locate 4</subuserid>
        <sourceid>2017-02-04 00:00:01</sourceid>
        <groupid>15</groupid>
        <account>138969</account>
      </account>
      <data>
        <first>RAYMOND</first>
        <last>WHITE</last>
        <address>1280 CEDAR</address>
        <city>WOOD RIVER</city>
        <state>IL</state>
        <zip>62095</zip>
        <phone>None</phone>
        <social>342567527</social>
        <dob>19580420</dob>
        <email>None</email>
      </data>
    </input>
  </transaction>
</root>
"""

xml_2 = """
<root>
  <login>
    <userid>medly00003</userid>
    <password>cp96ah11wg18</password>
    <realtime>1</realtime>
    <protocol>1</protocol>
    <timeout>10</timeout>
    <sid>xtech:locate:consumer:4</sid>
    <output>account</output>
  </login>
  <transaction>
    <input>
      <account>
        <subuserid>Locate 4</subuserid>
        <sourceid>2017-02-04 00:00:01</sourceid>
        <groupid>15</groupid>
        <account>104503</account>
      </account>
      <data>
        <first>SHERELL</first>
        <last>MING</last>
        <address>8306 CROTON AVE</address>
        <city>TAMPA</city>
        <state>FL</state>
        <zip>33619</zip>
        <phone>None</phone>
        <social>595056738</social>
        <dob>19810605</dob>
        <email>None</email>
      </data>
    </input>
  </transaction>
</root>
"""

xml_3 = """
<root>
  <login>
    <userid>medly00003</userid>
    <password>cp96ah11wg18</password>
    <realtime>1</realtime>
    <protocol>1</protocol>
    <timeout>10</timeout>
    <sid>xtech:locate:consumer:4</sid>
    <output>account</output>
  </login>
  <transaction>
    <input>
      <account>
        <subuserid>Locate 4</subuserid>
        <sourceid>2017-02-04 00:00:01</sourceid>
        <groupid>15</groupid>
        <account>105510</account>
      </account>
      <data>
        <first>RAY</first>
        <last>DIAZ</last>
        <address>1000 W 45TH PL</address>
        <city>HIALEAH</city>
        <state>FL</state>
        <zip>33012</zip>
        <phone>None</phone>
        <social>593256292</social>
        <dob>19920811</dob>
        <email>None</email>
      </data>
    </input>
  </transaction>
</root>
"""

xml_inputs = []
xml_inputs.append(xml_1.strip())
xml_inputs.append(xml_2.strip())
xml_inputs.append(xml_3.strip())

def send_via_proxy(xml_req):
    result = None
    headers = {'Content-Type': 'application/xml'}   # Set what our server accepts
    proxies = {
      "https": EB_REAL_TIME_HTTPSPROXY,
      "http": EB_REAL_TIME_HTTPPROXY
    }
    print('proxy is set to {}'.format(EB_REAL_TIME_HTTPPROXY))
    try:
        results = requests.post(EB_REAL_TIME_URL,
                                verify=True,
                                data=xml_req,
                                headers=headers,
                                proxies=proxies)
    except requests.exceptions.ProxyError as e:
        print('Got proxy error: {}'.format(e))
        raise
        sys.exit(2)
    else:
        result = results.text
    return result


if __name__ == '__main__':
    for xml_req in xml_inputs:
        resp = send_via_proxy(xml_req)
        print(resp)    
