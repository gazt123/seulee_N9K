#!/usr/bin/env python
import sys
import syslog
from cli import *

diag = cli('show diagnostic result module 1 test SecondaryBootROM detail | grep Consecutive ')
cons = diag.split()[4]

if cons != '0':
	syslog.syslog(2, 'SecondaryBootROM ' + cons + ' Consecutive failure occurred')
else:
	pass

#event manager applet gold_SecondaryBR_log
#  event gold module all test SecondaryBootROM testing-type monitoring consecutive-failure 1
#  action 1 cli source background TOR_SecondaryBootROM_log_I76.py

#script by seulee
