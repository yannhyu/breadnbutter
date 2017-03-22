# test_async_requests.py
import grequests
import requests
from xml.dom import minidom

EB_REAL_TIME_URL = "https://factory.ebureau.com/test/"

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

HEADERS = {'Content-Type': 'application/xml'}

def prettify(rough_string):
    """Return a pretty-printed XML string for the Element.
    """
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")


if __name__ == '__main__':
    ses = requests.session()
    rs = [ grequests.post(EB_REAL_TIME_URL, session=ses, verify=True, data=xml_req, headers=HEADERS) for xml_req in xml_inputs ]

    greq_imaps = grequests.imap(rs, size=5)

    for greq_imap in greq_imaps:
        print(greq_imap.request.body)
        print(prettify(greq_imap.content))
