#!/usr/bin/env python
# -*- coding: utf-8 -*-

from xml.dom import minidom
import os

root = minidom.Document()
xml = root.createElement('root')
root.appendChild(xml)

productChild = root.createElement('product')
xml.appendChild(productChild)

productName = root.createElement('name')
productName.appendChild(root.createTextNode('Notebook'))
productChild.appendChild(productName)

productName = root.createElement('price')
productName.appendChild(root.createTextNode('9.00'))
productChild.appendChild(productName)

xml_str = root.toprettyxml(indent='\t')
print(xml_str)

file_save_path = 'test.xml'
with open(file_save_path, 'w') as fh:
    fh.write(xml_str)