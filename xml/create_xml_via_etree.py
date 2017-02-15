# create_xml_via_etree.py

from xml.etree.ElementTree import ElementTree
from xml.etree.ElementTree import Element
import xml.etree.ElementTree as etree

root = Element('person')
tree = ElementTree(root)

name = Element('name')
root.append(name)
name.text = 'Yann'
root.set('id', '123')

print(etree.tostring(root))
tree.write(open('person.xml', 'w'))