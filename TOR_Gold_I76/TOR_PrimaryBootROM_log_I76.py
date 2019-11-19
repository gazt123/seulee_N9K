#!/usr/bin/env python
import sys
import syslog
from cli import *

diag = cli('show diagnostic result module 1 test PrimaryBootROM detail | grep Consecutive  ')
cons = diag.split()[4]

if cons != '0':
	syslog.syslog(2, 'PrimaryBootROM ' + cons + ' Consecutive failure occurred')
else:
	pass

#event manager applet gold_PrimaryBR_log
#  event gold module all test PrimaryBootROM testing-type monitoring consecutive-failure 1
#  action 1 cli source background TOR_PrimaryBootROM_log_I76.py

#script by seulee
