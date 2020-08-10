# Fantom Node Monitor

This setup lets you monitor your fantom node. Key elements are of course the Grafana dashboard for visualization and Prometheus as data source. Prometheus provides interfaces for add-ons, of which the following are integrated.

- <a src="https://github.com/prometheus/node_exporter">node_exporter</a>: Provides general machine information about memory, cpu, file system etc

- <a src="https://github.com/block42-blockchain-company/lachesis_exporter">lachesis_exporter*</a>*: Uses the Lachesis API to provide Fantom specific metrics. Currently only the epoch is part of the metrics.

By spinning up the fantom node monitor, all configurations and dashboards are created and all exporters are started. Feel free to use our <a src="https://hub.docker.com/repository/docker/block42blockchaincompany/fantom-node-monitor">Docker Image</a>.
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

