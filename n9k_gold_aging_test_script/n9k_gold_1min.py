#!/usr/bin/env python
import sys
import time
import syslog
from cli import *

while True:
	cli('diagnostic start module 27 test 3,4 ; diagnostic start module 28 test 3,4 ')
	time.sleep (60)

"""
conf t
event manager applet GOLD_1MIN_TEST
event syslog pattern "gold_every_1min"
 action 1.0 cli source background n9k_gold_1min.py
"""

#logit gold_every_1min // for an initial trigger