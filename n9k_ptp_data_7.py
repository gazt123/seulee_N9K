#!/usr/bin/env python
import sys
import syslog
from cli import *

cli(' show clock >> bootflash:ptp_data7.txt ; show ptp corrections >> bootflash:ptp_data7.txt ')

ptp = cli(' show clock ; slot 1 debug hardware internal sug dump asic 0 slice 0 table tah_sug_pcx_cfg_el_ptp_clock ')
f=file('/bootflash/test77.txt', 'w')
f.write(ptp)
f.close()
cli(' show file bootflash:test77.txt >> bootflash:ptp_data77.txt ')

ptp1 = cli(' show clock ; slot 1 debug hardware internal sug dump asic 0 slice 0 table tah_sug_pcx_cfg_el_ptp_adj ')
f=file('/bootflash/test77.txt', 'w')
f.write(ptp1)
f.close()
cli(' show file bootflash:test77.txt >> bootflash:ptp_data77.txt ')

ptp2 = cli(' show clock ; slot 1 debug hardware internal sug dump asic 0 slice 0 table tah_sug_pcx_sta_el_ptp_clock_time ')
f=file('/bootflash/test77.txt', 'w')
f.write(ptp2)
f.close()
cli(' show file bootflash:test77.txt >> bootflash:ptp_data77.txt ')

ptp3 = cli(' show clock ; slot 1 debug hardware internal sug dump asic 0 slice 0 table tah_sug_pcx_cfg_el_ivxlan_timestamp ')
f=file('/bootflash/test77.txt', 'w')
f.write(ptp3)
f.close()
cli(' show file bootflash:test77.txt >> bootflash:ptp_data77.txt ')

ptp4 = cli(' show clock ; slot 1 debug hardware internal sug dump asic 0 slice 0 table tah_sug_pcx_cfg_el_erspan3_clock ')
f=file('/bootflash/test77.txt', 'w')
f.write(ptp4)
f.close()
cli(' show file bootflash:test77.txt >> bootflash:ptp_data77.txt ')

ptp5 = cli(' show clock ; slot 1 debug hardware internal sug dump asic 0 slice 0 table tah_sug_pcx_sta_el_ivxlan_timestamp ')
f=file('/bootflash/test77.txt', 'w')
f.write(ptp5)
f.close()
cli(' show file bootflash:test77.txt >> bootflash:ptp_data77.txt ')

ptp6 = cli(' show clock ; slot 1 debug hardware internal sug dump asic 0 slice 0 table tah_sug_pcx_dhs_el_ptp_clock ')
f=file('/bootflash/test77.txt', 'w')
f.write(ptp6)
f.close()
cli(' show file bootflash:test77.txt >> bootflash:ptp_data77.txt ')

ptp7 = cli(' show clock ; slot 1 debug hardware internal sug dump asic 0 slice 0 table tah_sug_pcx_dhs_el_ivxlan_timestamp ')
f=file('/bootflash/test77.txt', 'w')
f.write(ptp7)
f.close()
cli(' show file bootflash:test77.txt >> bootflash:ptp_data77.txt ')

ptp8 = cli(' show clock ; slot 1 debug hardware internal sug dump asic 0 slice 0 table tah_sug_pcx_cfg_ptp_sync ')
f=file('/bootflash/test77.txt', 'w')
f.write(ptp8)
f.close()
cli(' show file bootflash:test77.txt >> bootflash:ptp_data77.txt ')

ptp9 = cli(' show clock ; slot 1 debug hardware internal sug dump asic 0 slice 0 table tah_sug_pcx_cfg_ptp_clock ')
f=file('/bootflash/test77.txt', 'w')
f.write(ptp9)
f.close()
cli(' show file bootflash:test77.txt >> bootflash:ptp_data77.txt ')

ptp10 = cli(' show clock ; slot 1 debug hardware internal sug dump asic 0 slice 0 table tah_sug_pcx_CFG_el_pulse ')
f=file('/bootflash/test77.txt', 'w')
f.write(ptp10)
f.close()
cli(' show file bootflash:test77.txt >> bootflash:ptp_data77.txt ')

ptp11 = cli(' show clock ; slot 1 debug hardware internal sug dump asic 0 slice 0 table tah_sug_pcx_CFG_el_capture ')
f=file('/bootflash/test77.txt', 'w')
f.write(ptp11)
f.close()
cli(' show file bootflash:test77.txt >> bootflash:ptp_data77.txt ')

ptp12 = cli(' show clock ; slot 1 debug hardware internal sug dump asic 0 slice 0 table tah_sug_pcx_DHS_el_erspan3_clock ')
f=file('/bootflash/test77.txt', 'w')
f.write(ptp12)
f.close()
cli(' show file bootflash:test77.txt >> bootflash:ptp_data77.txt ')

ptp13 = cli(' show clock ; slot 1 debug hardware internal sug dump asic 0 slice 0 table tah_sug_pcx_STA_el_trig_clock ')
f=file('/bootflash/test77.txt', 'w')
f.write(ptp13)
f.close()
cli(' show file bootflash:test77.txt >> bootflash:ptp_data77.txt ')

ptp14 = cli(' show clock ; slot 1 debug hardware internal sug dump asic 0 slice 0 table tah_sug_pcx_CFG_sync ')
f=file('/bootflash/test77.txt', 'w')
f.write(ptp14)
f.close()
cli(' show file bootflash:test77.txt >> bootflash:ptp_data77.txt ')

#scheduler job name ptp_data_7
#source /bootflash/scripts/n9k_ptp_data_7.py
 
#end-job
 
#scheduler schedule name ptp_data_7
#  job name ptp_data_6
#time start 2019:01:05:00:00 repeat 0:0:1
