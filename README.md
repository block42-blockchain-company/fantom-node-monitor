# Fantom Node Monitor

The Fantom Node Monitor is currently in a mvp version.
It consists of a Grafana Dashboard, which will display the metrics
gained from Prometheus. Both are running in a docker container and 
using the host network. This may change in future versions.
<br>
By spinning up the node monitor, all configurations and dashboards are 
created for you. 
<br>
<br>
Note: Since this is a minimal version we have currently added the 
external module <a src="https://github.com/prometheus/node_exporter">node_exporter</a> to Prometheus as a data source.
Fantom specific metrics will follow as soon as the exporter for it is ready.

## Getting started

### Setup

Start the monitor with the following command:
```shell
python3 ./setup.py
```

You can view the dashboard by accessing the machine on port 3000.


### Tear Down
*Note: Be aware that the following will also remove all data collected!*
Stop the containers and remove all artifcats with:
```shell
python3 ./tear_down.py
```


