# Fantom Node Monitor

This setup lets you monitor your Fantom node. Key elements are the Grafana dashboard for visualization and Prometheus as data base. 
Prometheus provides interfaces for database agents, of which the following are integrated:

- [node_exporter](https://github.com/prometheus/node_exporter): Provides general machine information about memory, cpu, file system etc
- [lachesis_exporter](https://github.com/block42-blockchain-company/lachesis_exporter): Uses the Lachesis API to provide Fantom specific metrics. 
It is currently under development.

By spinning up the Fantom node monitor, all configurations and dashboards are created and all exporters are started.

## Getting started

### Setup

Make sure to have `docker` and `docker-compose` installed.

Start the monitor by typing the following command in your terminal:
```shell
docker-compose up -d
```

This will spin up a single docker container (using [fantom-node-monitor image](https://hub.docker.com/repository/docker/block42blockchaincompany/fantom-node-monitor)) 
including all necessary services and programs. 

### First Steps

Access your machine on port 3000. 
The first time you access the dashboard you will need to enter the default credentials and set a new password.
The default credentials are:

Username: admin <br>
Password: admin

Once you're logged in, you should see **Fantom Node Overview** in Dashboards. 
Please allow some time for the first metrics to be displayed.


### Tear Down
Stop the container with:
```shell
docker-compose down
```

Stop the container and remove all artifacts (including persistent volumes) with:

*Note: Be aware that the following will also remove all data collected!*
```shell
docker-compose down -v
```
