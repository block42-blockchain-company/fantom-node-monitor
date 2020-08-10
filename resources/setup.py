import subprocess
import os
from common import consts

# Start node_exporter
#command = "${GOPATH-$HOME/go}/src/github.com/prometheus/node_exporter/node_exporter --path.rootfs=/host"
#node_exporter = subprocess.Popen(command.split())

# Start Grafana Server
command = "service grafana-server start"
grafana_server = subprocess.Popen(command.split())

# Persist
command = "tail -f /dev/null"
node_monitor_startup = subprocess.Popen(command.split())
node_monitor_startup.wait()
