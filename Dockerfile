FROM ubuntu:18.04

RUN apt-get update


# --- INSTALL ---

# General
RUN apt-get install -y python3

# Grafana
RUN apt-get install -y apt-transport-https
RUN apt-get install -y software-properties-common wget
RUN wget -q -O - https://packages.grafana.com/gpg.key | apt-key add -
RUN echo "deb https://packages.grafana.com/oss/deb stable main" | tee -a /etc/apt/sources.list.d/grafana.list 

# Prometheus
RUN apt-get update
RUN apt-get install -y grafana


# --- Configure ---

# General
ADD . /home/

# Grafana
ADD ./resources/grafana/provisioning /etc/grafana/provisioning/
ADD ./resources/grafana//dashboard/fantom_overview.json /var/lib/grafana/dashboards/fantom_overview.json


#/prometheus/prometheus.yml:/etc/prometheus/prometheus.yml

CMD ["/home/resources/setup.py"]
ENTRYPOINT ["python3"]