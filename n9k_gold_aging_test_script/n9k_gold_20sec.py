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
		cli('diagnostic start module %s test 1 ' % m)
		result = result + 1

	cli('diagnostic start module 22 test 1 ; diagnostic start module 23 test 1 ; diagnostic start module 24 test 1 ; diagnostic start module 26 test 1 ')

	time.sleep (20)

"""
conf t
event manager applet GOLD_20SEC_TEST
event syslog pattern "gold_every_20sec"
 action 1.0 cli source background n9k_gold_20sec.py
"""

#logit gold_every_20sec // for an initial trigger