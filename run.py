import subprocess

print("==== Fantom Node Monitor Setup ====\n")

# "host" attributes necessary in order for node_exporter to access host machine metrics
'''
command = "docker volume create grafana-volume"
grafana_volume_creation = subprocess.Popen(command.split())

command = "docker volume create prometheus-volume"
prometheus_volume_creation = subprocess.Popen(command.split())

grafana_volume_creation.wait()
prometheus_volume_creation.wait()
'''

command = 'docker run -d \
  --net="host" \
  --pid="host" \
  -v "/:/host:ro,rslave" \
  --name ftm-node-monitor \
  fantom-node-monitor'

node_monitor_startup = subprocess.Popen(command.split())
node_monitor_startup.wait()

