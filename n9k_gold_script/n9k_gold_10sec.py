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
		cli('diagnostic start module %s test 8,11 ' % m)
		result = result + 1

	cli('diagnostic start module 22 test 8 ; diagnostic start module 23 test 8 ;\
	 diagnostic start module 24 test 8 ; diagnostic start module 26 test 8 ;\
	  diagnostic start module 27 test 13 ; diagnostic start module 28 test 13 ;\
	   diagnostic start module 29 test 6 ; diagnostic start module 30 test 6 ')

	time.sleep (10)

# GOLD Interval Change
# [MOD]FpgaRegTest(test8): 30sec. => 10 sec.
# [MOD]L2ACLRedirect(test11): 1min. => 10 sec.
# [FM]FpgaRegTest(test8): 30sec. => 10 sec.
# [SUP]FpgaRegTest(test13): 30sec. => 10 sec.
# [SC]FpgaRegTest(test6): 30sec. => 10 sec.

"""
conf t
event manager applet GOLD_10SEC_TEST
event syslog pattern "gold_every_10sec"
 action 1.0 cli source background n9k_gold_10sec.py
"""

#logit gold_every_10sec // for an initial trigger
