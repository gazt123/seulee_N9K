#!/usr/bin/env python
import sys
import time
import syslog
from cli import *

while True:
	cli('diagnostic start module 27 test 15 ; diagnostic start module 28 test 15 ')
	time.sleep (300)

# GOLD Interval Change
# [SUP]Mce(test15): 1min. => 20 sec.

"""
conf t
event manager applet GOLD_5MIN_TEST
event syslog pattern "gold_every_5min"
 action 1.0 cli source background n9k_gold_5min.py
"""

#logit gold_every_5min // for an initial trigger