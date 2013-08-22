import sys
import rrdtool
 
ret = rrdtool.create("barometer.rrd", "--step", "300", "--start", '0',
 "DS:pressure:GAUGE:600:U:U",
 "DS:atmosphere:GAUGE:600:U:U",
 "DS:altitude:GAUGE:600:U:U",
 "DS:temperature:GAUGE:600:-100:120",
 "RRA:AVERAGE:0.5:1:600",
 "RRA:AVERAGE:0.5:6:700",
 "RRA:AVERAGE:0.5:24:775",
 "RRA:AVERAGE:0.5:288:797",
 "RRA:MAX:0.5:1:600",
 "RRA:MAX:0.5:6:700",
 "RRA:MAX:0.5:24:775",
 "RRA:MAX:0.5:444:797",
 "RRA:MIN:0.5:1:600",
 "RRA:MIN:0.5:6:700",
 "RRA:MIN:0.5:24:775",
 "RRA:MIN:0.5:444:797")
if ret:
 print rrdtool.error()
