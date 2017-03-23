#!/usr/bin/env python

import xml.etree.ElementTree as ET
import sys

tree = ET.parse('small_test_nychalf2017.gpx')
root = tree.getroot()

print root

for child in root:
  for kids in child:
    for gkids in kids:
      print gkids.attrib
