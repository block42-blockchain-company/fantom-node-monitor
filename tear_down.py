import subprocess
from common import consts

print("==== Fantom Node Monitor Teardown ====\n")

command = "docker-compose down"
shutdown_container = subprocess.Popen(command.split())
shutdown_container.wait()

command = "lsof -ti tcp:{} | xargs kill".format(consts.NODE_EXPORTER_PORT)
shutdown_node_exporter = subprocess.Popen(command.split())

command = "docker volume rm grafana-volume"
rm_grafana_volume = subprocess.Popen(command.split())

command = "docker volume rm prometheus-volume"
rm_prometheus_volume = subprocess.Popen(command.split())

rm_grafana_volume.wait()
rm_prometheus_volume.wait()
shutdown_node_exporter.wait()

# TODO: Shut down Node_Exporter!

print("Teardown complete!")
