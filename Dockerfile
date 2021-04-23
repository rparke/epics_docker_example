FROM gcr.io/diamond-privreg/controls/prod/epics/epics-synapps

COPY --chown=1000 energy_calc energy_calc

RUN echo 'ENERGY_CALC=$(SUPPORT)/energy_calc' >> configure/RELEASE && \ 
   make release && \ 
   cd energy_calc && \
   make && \
   make clean




CMD ls
