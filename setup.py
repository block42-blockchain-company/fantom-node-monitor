import subprocess
from common import consts

print("==== Fantom Node Monitor Setup ====\n")

command = "docker network create monitoring"
#network_setup = subprocess.Popen(command.split())

command = "docker volume create grafana-volume"
grafana_volume_creation = subprocess.Popen(command.split())

command = "docker volume create prometheus-volume"
prometheus_volume_creation = subprocess.Popen(command.split())

#network_setup.wait()
grafana_volume_creation.wait()
prometheus_volume_creation.wait()


print("\n==== Start Grafana and Prometheus Container ====")
command = 'docker-compose up -d'
spin_up_containers = subprocess.Popen(command.split())
spin_up_containers.wait()


print("\n==== Download and Install Node_Exporter natively ====")

command = "wget https://github.com/prometheus/node_exporter/releases/download/v1.0.1/node_exporter-1.0.1.linux-amd64.tar.gz"
download_node_exporter = subprocess.Popen(command.split())
download_node_exporter.wait()

command = "tar -xzf ./node_exporter-1.0.1.linux-amd64.tar.gz -C ./binary"
unwrap_node_exporter = subprocess.Popen(command.split())
unwrap_node_exporter.wait()

command = "./binary/node_exporter-1.0.1.linux-amd64/node_exporter"
start_node_exporter = subprocess.Popen(command.split())


print("\n==== Setup complete! ====")
