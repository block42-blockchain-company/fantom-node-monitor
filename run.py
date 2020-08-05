import subprocess

print("==== Fantom Node Monitor Setup ====\n")

# "host" attributes necessary in order for node_exporter to access host machine metrics
command = "docker volume create grafana-volume"
grafana_volume_creation = subprocess.Popen(command.split())

command = "docker volume create prometheus-volume"
prometheus_volume_creation = subprocess.Popen(command.split())

grafana_volume_creation.wait()
prometheus_volume_creation.wait()

command = 'docker run -d \
  --net="host" \
  --pid="host" \
  -v "/:/host:ro,rslave" \
  -v grafana-volume:/var/lib/grafana \
  -v prometheus-volume:/prometheus \
  fantom-node-monitor\
  --path.rootfs=/host'

node_monitor_startup = subprocess.Popen(command.split())
node_monitor_startup.wait()

# Persist
command = "tail -f /dev/null"
node_monitor_startup = subprocess.Popen(command.split())
