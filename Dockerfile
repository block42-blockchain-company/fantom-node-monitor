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

RUN go get github.com/godbus/dbus
RUN go get github.com/prometheus/node_exporter ; exit 0
RUN make /go/src/github.com/prometheus/node_exporter


# --- Configure ---

# General
ADD . /home/

# Grafana
ADD ./resources/grafana/provisioning /etc/grafana/provisioning/
ADD ./resources/grafana//dashboard/fantom_overview.json /var/lib/grafana/dashboards/fantom_overview.json


#/prometheus/prometheus.yml:/etc/prometheus/prometheus.yml

CMD ["/home/resources/setup.py"]
ENTRYPOINT ["python3"]