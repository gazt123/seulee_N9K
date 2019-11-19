#!/usr/bin/env python
import sys
import syslog
from cli import *

diag = cli('show diagnostic result module 1 test BootFlash detail | grep Consecutive ')
cons = diag.split()[4]

if cons != '0':
	syslog.syslog(2, 'BootFlash ' + cons + ' Consecutive failure occurred')
else:
	pass

#event manager applet gold_BootFlash_log
#  event gold module all test BootFlash testing-type monitoring consecutive-failure 1
#  action 1 cli source background TOR_BootFlash_log_I76.py

#script by seulee
