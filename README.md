# Fantom Node Monitor

The Fantom Node Monitor is currently in a mvp version.
Its key elements are of course the Grafana dashboard for visualization and Prometheus as data source. 
Prometheus provides interfaces for add-ons. Currently <a src="https://github.com/prometheus/node_exporter">node_exporter</a>
as well as the currently mvp version of the lachesis_exporter.
- *node_exporter*: Provides general machine information about memory, cpu, file system etc
- *lachesis_exporter*: Uses the Lachesis API to provide Fantom specific metrics. Currently only the epoch is part of the metrics.

By spinning up the fantom node monitor, all configurations and dashboards are 
created and all exporters are started.
<br>

## Getting started

### Setup

Start the monitor with the following command:
```shell
python3 setup.py
```

This will spinn up a single docker container including all necessary services and programs.

You can view the dashboard by accessing the machine on port 3000.
Log in to Grafana using the username "admin" and password "admin".
The Fantom Node Overview Dashboard should be visible to you. 
It may take some time until the first metrics arrive and are displayed.


### Tear Down
*Note: Be aware that the following will also remove all data collected!*
Stop the containers and remove all artifcats with:
```shell
python3 tear_down.py
```

## Current State
Both Grafana and Prometheus are running in a docker container and using the host network in order to communicate with the exporter.
It is best practise to keep the exporters as close to the application as possible.
<br>
This is a minimal version so the whole codebase is likely to change when aiming for a production version!

backup
# Golang
RUN mkdir /home/go
RUN cd /tmp
RUN wget https://dl.google.com/go/go1.14.6.linux-amd64.tar.gz
RUN tar -xvf go1.14.6.linux-amd64.tar.gz
RUN mv go /usr/local
RUN export GOROOT=/usr/local/go
RUN export GOPATH=$HOME/go
RUN export PATH=$GOPATH/bin:$GOROOT/bin:$PATH
RUN . ~/.profile
RUN go version