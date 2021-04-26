FROM gcr.io/diamond-privreg/controls/prod/epics/epics-synapps

COPY --chown=1000 energy_calc energy_calc
COPY --chown=1000 BL46P-EA-IOC-03 BL46P-EA-IOC-03


RUN echo 'ENERGY_CALC=$(SUPPORT)/energy_calc' >> configure/RELEASE && \
   echo 'BL46P=$(SUPPORT)/BL46P-EA-IOC-03' >> configure/RELEASE && \ 
   make release && \ 
   make -C energy_calc && \
   make -C energy_calc clean && \
   make -C BL46P-EA-IOC-03




COPY --chown=1000 launch_and_boot/stBL46P-EA-IOC-03.sh BL46P-EA-IOC-03/bin/linux-x86_64/stBL46P-EA-IOC-03.sh
COPY --chown=1000 launch_and_boot/stBL46P-EA-IOC-03.boot BL46P-EA-IOC-03/bin/linux-x86_64/stBL46P-EA-IOC-03.boot
COPY --chown=1000 launch_and_boot/BL46P-EA-IOC-03_expanded.db BL46P-EA-IOC-03/db/BL46P-EA-IOC-03_expanded.db
 


CMD ./BL46P-EA-IOC-03/bin/linux-x86_64/stBL46P-EA-IOC-03.sh
