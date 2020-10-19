FROM golang:1.14.7

# --- INSTALL ---
# General
RUN apt-get update
RUN apt-get install -y git wget python3

# Grafana
RUN apt-get install -y apt-transport-https
RUN apt-get install -y software-properties-common
RUN wget -q -O - https://packages.grafana.com/gpg.key | apt-key add -
RUN echo "deb https://packages.grafana.com/oss/deb stable main" | tee -a /etc/apt/sources.list.d/grafana.list
RUN apt-get update
RUN apt-get install -y grafana

# Prometheus
RUN wget https://github.com/prometheus/prometheus/releases/download/v2.20.1/prometheus-2.20.1.linux-amd64.tar.gz
RUN tar xvf prometheus-2.20.1.linux-amd64.tar.gz
RUN cp prometheus-2.20.1.linux-amd64/prometheus /usr/local/bin/
RUN cp prometheus-2.20.1.linux-amd64/promtool /usr/local/bin/
RUN cp -r prometheus-2.20.1.linux-amd64/consoles /etc/prometheus
RUN cp -r prometheus-2.20.1.linux-amd64/console_libraries /etc/prometheus
RUN rm -rf prometheus-2.20.1.linux-amd64.tar.gz prometheus-2.20.1.linux-amd64

# Node Exporter
RUN go get github.com/godbus/dbus
RUN go get github.com/prometheus/node_exporter ; exit 0
RUN make /go/src/github.com/prometheus/node_exporter

# Lachesis Exporter
ARG lachesis_exporter_path=/go/src/github.com/block42-blockchain-company/lachesis_exporter
RUN mkdir -p $lachesis_exporter_path
RUN git clone https://github.com/block42-blockchain-company/lachesis_exporter.git  $lachesis_exporter_path
RUN cd $lachesis_exporter_path && git checkout feature/metrics
RUN go get -u $lachesis_exporter_path
RUN go install $lachesis_exporter_path
#RUN go get github.com/block42-blockchain-company/lachesis_exporter
#RUN go intsall github.com/block42-blockchain-company/lachesis_exporter

# --- Configure ---
# Grafana
ADD ./resources/grafana/provisioning /etc/grafana/provisioning/
ADD ./resources/grafana/dashboard/fantom_overview.json /var/lib/grafana/dashboards/fantom_overview.json

# Prometheus
RUN mkdir /data
ADD ./resources/prometheus/prometheus.yml /etc/prometheus/prometheus.yml

# Start exporters script
ADD ./resources/run.sh /home/


CMD bash /home/run.sh