#Makefile at top of application tree
TOP = .

include $(TOP)/configure/CONFIG

DIRS := $(DIRS) $(filter-out $(DIRS), configure)
DIRS := $(DIRS) $(filter-out $(DIRS), $(wildcard *App))
DIRS := $(DIRS) $(filter-out $(DIRS), $(wildcard iocBoot))

define DIR_template
 $(1)_DEPEND_DIRS = configure
endef
$(foreach dir, $(filter-out configure,$(DIRS)),$(eval $(call DIR_template,$(dir))))

iocBoot_DEPEND_DIRS += $(filter %App,$(DIRS))

# Comment out the following lines to disable creation of example iocs and documentation
DIRS := $(DIRS) $(filter-out $(DIRS), $(wildcard etc))

ifeq ($(wildcard etc),etc)
	include $(TOP)/etc/makeIocs/Makefile.iocs
	UNINSTALL_DIRS += $(IOC_DIRS)
endif

# Comment out the following line to disable building of example iocs
DIRS := $(DIRS) $(filter-out $(DIRS), $(wildcard iocs))


data/stBL46P-gui: $(DIRS) iocs/BL46P-EA-IOC-01/bin/linux-x86_64/stBL46P-EA-IOC-01-gui iocs/BL47P-EA-IOC-01/bin/linux-x86_64/stBL47P-EA-IOC-01-gui iocs/BL48P-EA-IOC-01/bin/linux-x86_64/stBL48P-EA-IOC-01-gui iocs/BL49P-EA-IOC-01/bin/linux-x86_64/stBL49P-EA-IOC-01-gui
	BL46PApp/opi/edl/makeSynoptic.py

include $(TOP)/configure/RULES_TOP
