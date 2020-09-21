import subprocess as sp
import os
from common import consts
#
# Start node_exporter
# TODO Create Service for node_exporter
#command = "node_exporter --path.rootfs=/host"
#node_exporter = sp.Popen(command.split())

# node_exporter = sp.Popen("ls /home/".split())
exec = sp.Popen("bash /home/run.sh".split())
#sp.Popen("./home/run.sh".split())
#node_exporter = sp.Popen("ls".split())


# sp.Popen("ls /go/bin/".split()).wait() # node-exporter binary
# print("------------")
# sp.Popen("ls /usr/lib/systemd/system".split()).wait() # grafana-server binary
# node_exporter = sp.Popen("service node-exporter start".split())
# node_exporter = sp.Popen("service node-exporter status".split())
# node_exporter = sp.Popen("/go/bin/node_exporter --path.rootfs=/host".split())
# node_exporter = sp.Popen("ls /usr/share/grafana".split())
# print(node_exporter.returncode)

# command = "whoami"
# node_exporter = sp.Popen(command.split())

# command = "update-rc.d node-exporter defaults"
# node_exporter = sp.Popen(command.split()).wait()
#
# command = "service node-exporter start"
# node_exporter = sp.Popen(command.split()).wait()

# command = "systemctl enable node-exporter.service"
# node_exporter = sp.Popen(command.split()).wait()
# # node_exporter.wait()
# # print(node_exporter.returncode)
#
# command = "systemctl start node-exporter.service"
# node_exporter = sp.Popen(command.split())
#
# command = "systemctl status node-exporter.service"
# node_exporter = sp.Popen(command.split())
#
# command = "systemctl status node-exporter"
# node_exporter = sp.Popen(command.split())
# node_exporter.wait()
# print(node_exporter.returncode)

# command = "cat /etc/init.d/grafana-server"
# node_exporter = sp.Popen(command.split())


# # TODO Create Service for lachesis_exporter
command = "lachesis_exporter"
node_exporter = sp.Popen(command.split())
node_exporter.wait()
print(node_exporter.returncode)
#
#
# Start Grafana Server
#command = "service grafana-server start"
#grafana_server = sp.Popen(command.split())
#
# Start Prometheus
# # TODO Create Service for Prometheus
# command = "prometheus \
# --config.file=/etc/prometheus/prometheus.yml \
# --storage.tsdb.path=/data"
# prometheus = sp.Popen(command.split())
#
#
# # Persist
# command = "tail -f /dev/null"
# node_monitor_startup = sp.Popen(command.split())
# node_monitor_startup.wait()
