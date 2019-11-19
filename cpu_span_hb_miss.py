#!/usr/bin/python
import sys
import syslog
from cli import *

"""
conf t
no event manager applet EOBC_HB_MISS
event manager applet EOBC_HB_MISS
event syslog pattern "Sup HB miss"
 action 1.0 syslog priority notifications msg EEM_TRIGGERED
 action 2.0 cli enable
 action 2.1 cli show ver > bootflash:mgmtspan.txt
"""

match_trigger = "No su"
num = 0

# Do an initial check for the file
file_check = cli('dir bootflash:/mgmtspan.txt')
if file_check[0:5] == match_trigger:
    num = 1
# While the first 5 characters of the output match "No su" (No such file or directory)
while num > 0:
    # Run the first ethanalyzer
    cli('ethanalyzer local interface mgmt limit-captured-frames 5000 write bootflash:mgmt_span1.pcap')
    # Check if the file is there
    file_check = cli('dir bootflash:/mgmtspan.txt')
    # If the file is not present
    if file_check[0:5] == match_trigger:
        # Delete our first ethanalyzer
        syslog.syslog(1, 'MGMT_SPAN_before_event')
        cli('delete bootflash:/mgmt_span1.pcap')
    # If the file is present:
    else:
        # Run the ethanalyzer and break the loop
        syslog.syslog(1, 'MGMT_SPAN_after_event')
        cli('ethanalyzer local interface mgmt limit-captured-frames 5000 write bootflash:mgmt_span2.pcap')
        break