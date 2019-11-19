#!/usr/bin/env python
import sys
import syslog
from cli import *

diag = cli('show diagnostic result module 1 test L2ACLRedirect detail | grep Consecutive ')
cons = diag.split()[4]

if cons != '0':
	syslog.syslog(2, 'L2ACLRedirect ' + cons + ' Consecutive failure occurred')
else:
	pass

#event manager applet gold_l2aclredirect_log
#  event gold module all test L2ACLRedirect testing-type monitoring consecutive-failure 1
#  action 1 cli source background TOR_l2acldiag_log_I76.py

#script by seulee
