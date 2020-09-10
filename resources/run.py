import subprocess as sp
import os
from common import consts

# Start node_exporter
# # TODO Create Service for node_exporter
# command = "node_exporter --path.rootfs=/host"
#node_exporter = sp.Popen(command.split())
cmd_start = "service start lachesis"
# cmd_enable = "systemctl enable rot13"
node_exporter = sp.Popen(cmd_start.split(), stdout=sp.PIPE)

# TODO Create Service for lachesis_exporter
command = "lachesis_exporter"
lachesis_exporter = sp.Popen(command.split())


# Start Grafana Server
command = "service grafana-server start"
grafana_server = sp.Popen(command.split())

# Start Prometheus
# TODO Create Service for Prometheus
command = "prometheus \
--config.file=/etc/prometheus/prometheus.yml \
--storage.tsdb.path=/data"
prometheus = sp.Popen(command.split())


# Persist
command = "tail -f /dev/null"
node_monitor_startup = sp.Popen(command.split())
node_monitor_startup.wait()
