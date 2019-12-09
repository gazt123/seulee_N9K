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

cli('echo ############### >> bootflash:fabric_asic_mon.txt ; show clock >> bootflash:fabric_asic_mon.txt ; echo ############### >> bootflash:fabric_asic_mon.txt')


while result < j:

	m = modules.pop()

	asic_e = cli(' show hardware internal fabric interface asic counters module %s | grep X | count' % m)
	asic_ei = int(asic_e)

	result = result + 1

	if asic_ei == 0:

		cli(' echo slot_%s_no_asic_error >> bootflash:fabric_asic_mon.txt' % m)

	else:
				
		cli(' show clock >> bootflash:fabric_asic_mon.txt')
				
		fme = cli(' show hardware internal fabric interface asic counters module %s | grep -a 3 Interface' % m)
		f=file('/bootflash/asic_err.txt', 'w')
		f.write(fme)
		f.close()
		cli(' show file bootflash:asic_err.txt >> bootflash:fabric_asic_mon.txt ')
				
		fme = cli(' show hardware internal fabric interface asic counters module %s | grep X' % m)
		f=file('/bootflash/asic_err.txt', 'w')
		f.write(fme)
		f.close()
		cli(' show file bootflash:asic_err.txt >> bootflash:fabric_asic_mon.txt ')
				
		fme = cli(' show hardware internal fabric interface asic counters module %s | grep -a 10 Conditions' % m)
		f=file('/bootflash/asic_err.txt', 'w')
		f.write(fme)
		f.close()
		cli(' show file bootflash:asic_err.txt >> bootflash:fabric_asic_mon.txt ')

		syslog.syslog(1, 'fabric asic error occurred in slot %s. Please check bootflash:fabric_asic_mon.txt ' % m)

		cli(' clear hardware internal fabric interface-all asic counters module %s ' % m)





#feature scheduler
#scheduler job name fabric_asic_mon
# source background /bootflash/scripts/fabric_asic_mon_v2.py
#scheduler schedule name fabric_asic_mon
#  job name fabric_asic_mon
#  time start now repeat 0:24:00


#script by seulee
