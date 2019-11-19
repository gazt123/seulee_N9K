#!/usr/bin/env python
import sys
import syslog
from cli import *

ptp = cli('show ptp corrections')
ptp1 = ptp.split()
cor = ptp1.pop(22)

if cor >= 100000000:
	cli('config terminal ; interface ethernet 1/27 ; shutdown ; sleep 2 ; no shutdown ; no scheduler schedule name ptp_failover2 ; end')
	syslog.syslog(1, 'ptp was failovered by resetting ptp interface')
else:
	cli('show clock >> bootflash:ptp_failover2.txt')


#(config)# feature schedular
#(config)# scheduler job name ptp_failover2
#(config-job)# source /bootflash/scripts/ptp_failover2.py
#(config-job)# exit
#(config)# scheduler schedule name ptp_failover2
#(config-schedule)# job name ptp_failover2
#(config-schedule)# time start now repeat 03
#(config-schedule)# exit



#script by seulee
