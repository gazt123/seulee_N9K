#!/usr/bin/env python
import sys
import syslog
from cli import *

syslog.syslog(1, 'resetting interface for testing - start')
cli('configure terminal ; interface ethernet 1/3-4 ; shut ; sleep 80 ; interface ethernet 1/3-4 ; no shut ')
syslog.syslog(1, 'resetting interface for testing - done')