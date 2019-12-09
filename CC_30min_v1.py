#!/usr/bin/env python
import sys
import syslog
import time
from cli import *

gold = 0
i = 0
j = 0
modules = ['m']
result = 1

while gold < 27:
	mod = cli('show module | grep 7.0(3)I7(7) ')
	gold = mod.split()[i]
	modules.append(gold)
	gold = int(gold)
	i = i + 4
	j = j + 1
modules.remove('m')
modules.remove('27')
modules.reverse()

while True:

	ccf = cli(' show consistency-checker link-state fabric-ieth | grep FAILED | count ')
	ccfi = int(ccf)

	if ccfi == 0:
		syslog.syslog(3, 'fabric-ieth CC status is ok')
		cli(' show clock >> bootflash:CC_good_status.txt \
			; show consistency-checker link-state fabric-ieth >> bootflash:CC_good_status.txt \
			; echo ######################## >> bootflash:CC_good_status.txt ')
	else:

		modules1 = modules

		while result < j:
			m = modules1.pop()
			
			fme = cli(' slot %s show hardware internal tah ieth link status ' % m)
			f=file('/bootflash/CC.txt', 'w')
			f.write(fme)
			f.close()
			cli(' show file bootflash:CC.txt >> bootflash:CC_bad_status.txt ')
			
			fme = cli(' show system internal interface counters detail module %s ' % m)
			f=file('/bootflash/CC.txt', 'w')
			f.write(fme)
			f.close()
			cli(' show file bootflash:CC.txt >> bootflash:CC_bad_status.txt ')
			
			fme = cli(' show hardware internal fabric interface asic counters module %s ' % m)
			f=file('/bootflash/CC.txt', 'w')
			f.write(fme)
			f.close()
			cli(' show file bootflash:CC.txt >> bootflash:CC_bad_status.txt ')
			
			result = result + 1

		cli(' show clock >> bootflash:CC_bad_status.txt \
			; show consistency-checker link-state fabric-ieth >> bootflash:CC_bad_status.txt \
			; show hardware internal errors all >> bootflash:CC_bad_status.txt \
			; echo ######################## >> bootflash:CC_bad_status.txt')

		syslog.syslog(1, 'fabric-ieth CC status is NOT ok. Please check bootflash:CC_bad_status.txt ')

	time.sleep (1800)


#event manager applet CC_30min
#  event syslog pattern "ASCII-CFG-2-CONF_CONTROL: System ready"
#  action 1 cli source background CC_30min_v1.py

#script by seulee
