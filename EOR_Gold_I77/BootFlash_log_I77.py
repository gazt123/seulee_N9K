#!/usr/bin/env python
import sys
import syslog
from cli import *

mod = cli('show module | egrep SUP1|SUP2 ')
mod1 = mod.split()

if mod1.count('27') == 1:
	diag = cli('show diagnostic result module 27 test BootFlash detail | grep Consecutive ')
	cons = diag.split()[4]

	if cons != '0':
		syslog.syslog(2, 'Slot 27 BootFlash ' + cons + ' Consecutive failure occurred')
	else:
		pass
else:
	pass

if mod1.count('28') == 1:
	diag = cli('show diagnostic result module 28 test BootFlash detail | grep Consecutive ')
	cons = diag.split()[4]

	if cons != '0':
		syslog.syslog(2, 'Slot 28 BootFlash ' + cons + ' Consecutive failure occurred')
	else:
		pass
else:
	pass	


#event manager applet gold_BootFlash_log
#  event gold module all test BootFlash testing-type monitoring consecutive-failure 1
#  action 1 cli source background BootFlash_log_I77.py

#It's for SUPs.
#script by seulee
