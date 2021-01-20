# Fantom Node Monitor

This setup lets you monitor your Fantom node. Key elements are the Grafana dashboard for visualization and Prometheus as data base. Prometheus provides interfaces for database agents, of which the following are integrated.

- <a src="https://github.com/prometheus/node_exporter">node_exporter</a>: Provides general machine information about memory, cpu, file system etc
- <a src="https://github.com/block42-blockchain-company/lachesis_exporter">lachesis_exporter</a> : Uses the Lachesis API to provide Fantom specific metrics. It is currently under development.

By spinning up the Fantom node monitor, all configurations and dashboards are created and all exporters are started.
<br>

## Getting started

### Build
Start the docker build:
```shell
python3 main.py build
```

This will build a docker image from the Dockerfile.

### Setup

Start the monitor with the following command:
```shell
python3 main.py setup
```

This will spinn up a single docker container (using <a src="https://hub.docker.com/repository/docker/block42blockchaincompany/fantom-node-monitor">fantom-node-monitor image</a>) including all necessary services and programs. 

### First Steps

Access your machine on port 3000. 
The first time you access the dashboard you will need to enter the default credentials and set a new password.
The default credentials are:

Username: admin <br>
Password: admin

Once you're logged in, you should see **Fantom Node Overview** in Dashboards. Please allow some time for the first metrics to be displayed.


### Tear Down
*Note: Be aware that the following will also remove all data collected!*
Stop the containers and remove all artifcats (including persistent volumes) with:

```shell
python3 main.py teardown
```
