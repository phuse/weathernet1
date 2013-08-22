#!/usr/bin/python
import xml.etree.ElementTree as etree
import urllib2
import sys
import time
import rrdtool
xml = urllib2.urlopen("http://192.168.1.33/xml")
xml2 = xml.read()
options = dict((e.tag, e.text) for e in etree.fromstring(xml2))
#print options
#print float(options['Temp'])+float(options['Altitude'])
ret = rrdtool.update('barometer.rrd','N:' + `int(options['Pressure'])` + ':' + `float(options['Atmosphere'])`  + ':' + `float(options['Altitude'])` + ':' + `float(options['Temp'])`);
if ret:
 print rrdtool.error()

ret = rrdtool.graph( "public_html/Daily-Temp.png", "--start", "-1d", "--vertical-label=Celcius",
 "DEF:temp=barometer.rrd:temperature:AVERAGE",
 "AREA:temp#00FF00:temperature",
 "COMMENT:\\n")
ret = rrdtool.graph( "public_html/Daily-Pressure.png", "--start", "-1d", "--vertical-label=Pascal",
 "DEF:pressure=barometer.rrd:pressure:AVERAGE",
 "AREA:pressure#00FF00:pressure",
 "COMMENT:\\n")
