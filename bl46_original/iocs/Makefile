TOP = ..
include $(TOP)/configure/CONFIG

include $(TOP)/etc/makeIocs/Makefile.iocs

DIRS := $(wildcard $(IOCS))

include $(TOP)/configure/RULES_DIRS

#sed -i -e 's/BL49P-EA-IOC-01Top.edl/"-m dom=BL49P BL46P-synoptic.edl"/g' iocs/BL49P-EA-IOC-01/bin/linux-x86_64/stBL49P-EA-IOC-01-gui 
