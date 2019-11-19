#!/usr/bin/env python
import sys
import syslog
from cli import *
import time

def downup(interface):
	cli('config terminal ; interface %s ; shutdown ; sleep 2 ; no shutdown ; end' % interface)
	syslog.syslog(1, 'Interface ' + interface + ' resetted by Script')
	time.sleep(5)

with open('/proc/uptime', 'r') as f:
	uptime = float(f.readline().split()[0])


msg = sys.argv[1]
msg1 = msg.split()
for i in msg1:
	if 'Ethernet' in i:
		intf = i

downup(intf)

while uptime > 300:
	syslog.syslog(1, 'Attempting')
	cmd = 'show interface ' + intf + ' brief | grep up'
	output = cli(cmd)
	output = output.strip('\n')
	if output:
		syslog.syslog(1, 'Interface ' + intf + ' recovered by Script')
		break 
	downup(intf)

#event manager applet Reset_INT
#  event syslog pattern "LINK_FAILURE"
#  action 1 cli sleep 1
#  action 2 cli source reset_int-2nd.py "$_syslog_msg"