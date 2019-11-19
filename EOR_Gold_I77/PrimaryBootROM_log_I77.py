#!/usr/bin/env python
import sys
import syslog
from cli import *

gold = 0
i = 0
j = 0
modules = ['m']
result = 1

while gold != 30:
	mod = cli('show module | grep 7.0(3)I7(7) ')
	gold = mod.split()[i]
	modules.append(gold)
	gold = int(gold)
	i = i + 4
	j = j + 1

modules.remove('m')
modules.reverse()

while result < j:

	m = modules.pop()
	diag = cli('show diagnostic result module %s test 2 detail | grep Consecutive  ' % m)
	cons = diag.split()[4]

	if cons != '0':
		syslog.syslog(2, 'Slot ' + m + ' PrimaryBootROM ' + cons + ' Consecutive failure occurred')
	else:
		pass
	
	result = result + 1


#event manager applet gold_PrimaryBR_log
#  event gold module all test PrimaryBootROM testing-type monitoring consecutive-failure 1
#  action 1 cli source background PrimaryBootROM_log_I77.py

#It's for IO modules, FMs, SUPs and SCs.
#script by seulee
