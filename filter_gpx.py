#!/usr/bin/env python

import xml.etree.ElementTree as ET
import sys

tree = ET.parse('test.gpx')
root = tree.getroot()

for trkpt in root.iter('{http://www.topografix.com/GPX/1/1}trkpt'):
  lon = trkpt.attrib.get('lon')
  lat = trkpt.attrib.get('lat')
  time = trkpt[1].text
  print lon, lat, time
