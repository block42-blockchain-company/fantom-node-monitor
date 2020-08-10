import subprocess
import os
from common import consts

# Start node_exporter
# TODO Create Service for node_exporter
command = "node_exporter --path.rootfs=/host"
node_exporter = subprocess.Popen(command.split())

# TODO Create Service for lachesis_exporter

# Start Grafana Server
command = "service grafana-server start"
grafana_server = subprocess.Popen(command.split())

# Start Prometheus
# TODO Create Service for Prometheus
command = "prometheus --config.file=/etc/prometheus/prometheus.yml"
prometheus = subprocess.Popen(command.split())


# Persist
command = "tail -f /dev/null"
node_monitor_startup = subprocess.Popen(command.split())
node_monitor_startup.wait()
