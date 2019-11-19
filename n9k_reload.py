#!/usr/bin/env python
import sys
import time
import syslog
from cli import *

"""
event manager applet RELOAD
event syslog pattern "MODULE-5-ACTIVE_SUP_OK"
 action 1.0 cli sleep 900
 action 2.0 cli logit gold_every_10s
 action 3.0 cli sleep 1
 action 4.0 cli logit gold_every_1m
 action 5.0 cli sleep 129600
 action 6.0 cli source background n9k_reload.py
"""

cli('reload ; y ')
