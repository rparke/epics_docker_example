FROM gcr.io/diamond-privreg/controls/prod/epics/epics-synapps

COPY --chown=1000 energy_calc energy_calc

RUN echo 'ENERGY_CALC=$(SUPPORT)/energy_calc' >> configure/RELEASE && \ 
   make release && \ 
   cd energy_calc && \
   make && \
   make clean


COPY --chown=1000 bl46p-builder bl46p-builder

RUN echo 'BL46 = $(SUPPORT)/bl46p-builder' >> configure/RELEASE && \
   make release && \
   cd bl46p-builder && \
   make && \
   make clean


CMD ls
