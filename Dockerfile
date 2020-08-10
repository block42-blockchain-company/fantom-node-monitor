FROM ubuntu:18.04

# --- INSTALL ---

# General
RUN apt-get update
RUN apt-get install -y git wget python3


# Golang
RUN mkdir /home/go
RUN apt install golang -y
#RUN cd /tmp
#RUN wget https://dl.google.com/go/go1.14.6.linux-amd64.tar.gz
#RUN tar -xvf go1.14.6.linux-amd64.tar.gz
#RUN mv go /usr/local
RUN export GOROOT=/usr/lib/go
RUN export GOPATH=$HOME/go
RUN export PATH=$GOPATH/bin:$GOROOT/bin:$PATH
#RUN . ~/.profile


# Grafana
RUN apt-get install -y apt-transport-https
RUN apt-get install -y software-properties-common
RUN wget -q -O - https://packages.grafana.com/gpg.key | apt-key add -
RUN echo "deb https://packages.grafana.com/oss/deb stable main" | tee -a /etc/apt/sources.list.d/grafana.list
RUN apt-get update
RUN apt-get install -y grafana

RUN go get github.com/godbus/dbus
RUN go get github.com/prometheus/node_exporter ; exit 0
RUN make ${GOPATH-$HOME/go}/src/github.com/prometheus/node_exporter


# --- Configure ---

# General
ADD . /home/

# Grafana
ADD ./resources/grafana/provisioning /etc/grafana/provisioning/
ADD ./resources/grafana//dashboard/fantom_overview.json /var/lib/grafana/dashboards/fantom_overview.json


#/prometheus/prometheus.yml:/etc/prometheus/prometheus.yml

CMD ["/home/resources/setup.py"]
ENTRYPOINT ["python3"]