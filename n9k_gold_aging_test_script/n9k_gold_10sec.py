#!/usr/bin/env python
import sys
import time
import syslog
from cli import *

while True:
	gold = 0
	i = 0
	j = 0
	modules = ['m']
	result = 1

	while gold < 22:
		mod = cli('show module | grep 7.0(3)I7(6) ')
		gold = mod.split()[i]
		modules.append(gold)
		gold = int(gold)
		i = i + 4
		j = j + 1

	modules.remove('m')
	modules.remove('22')
	modules.reverse()

	while result < j:
		m = modules.pop()
		cli('diagnostic start module %s test 11 ' % m)
		result = result + 1

	time.sleep (10)


"""
conf t
event manager applet GOLD_10SEC_TEST
event syslog pattern "gold_every_10sec"
 action 1.0 cli source background n9k_gold_10sec.py
"""

#logit gold_every_10sec // for an initial trigger
