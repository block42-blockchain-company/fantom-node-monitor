#!/usr/bin/env python

import subprocess
import os
from common import consts


print("==== Fantom Node Monitor Setup ====\n")

command = "docker volume create grafana-volume"
grafana_volume_creation = subprocess.Popen(command.split())

command = "docker volume create prometheus-volume"
prometheus_volume_creation = subprocess.Popen(command.split())

grafana_volume_creation.wait()
prometheus_volume_creation.wait()


print("\n==== Start Grafana and Prometheus Container ====")
command = 'docker-compose up -d'
spin_up_containers = subprocess.Popen(command.split())
spin_up_containers.wait()


print("\n==== Start Lachesis_Exporter ====")
command = "./{}/lachesis_exporter/lachesis_exporter_linux_amd64".format(consts.BINARY_FOLDER)
start_lachesis_exporter = subprocess.Popen(command.split())

print("\n==== Start Node_Exporter ====")
command = 'docker run -d \
  --net="host" \
  --pid="host" \
  -v "/:/host:ro,rslave" \
  quay.io/prometheus/node-exporter \
  --path.rootfs=/host \
  --restart unless-stopped \
  --name node_exporter'
start_node_exporter = subprocess.Popen(command.split())

print("\n==== Setup complete! ====")
