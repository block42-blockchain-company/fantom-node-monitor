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


print("\n==== Download and Install Node_Exporter natively ====")

dir_path = os.path.dirname(os.path.realpath(__file__))
if not os.path.isdir(dir_path + consts.BINARY_FOLDER):
    command = "mkdir {}".format(consts.BINARY_FOLDER)
    mkdir = subprocess.Popen(command.split())
    mkdir.wait()

if not os.path.exists(dir_path + consts.BINARY_FOLDER + consts.NODE_EXPORTER_TAR_FILE):
    print("Downloading Node_Exporter 1.0.1")
    command = \
        "wget https://github.com/prometheus/node_exporter/releases/download/v1.0.1/{}" \
        " -P ./{}".format(consts.NODE_EXPORTER_TAR_FILE, consts.BINARY_FOLDER)
    download_node_exporter = subprocess.Popen(command.split())
    download_node_exporter.wait()

    command = "tar -xzf ./{}/{} -C {}".format(consts.BINARY_FOLDER, consts.NODE_EXPORTER_TAR_FILE, consts.BINARY_FOLDER)
    unwrap_node_exporter = subprocess.Popen(command.split())
    unwrap_node_exporter.wait()

    # TODO: Set up service for Node_Exporter
    command = "./binary/node_exporter-1.0.1.linux-amd64/node_exporter"
    start_node_exporter = subprocess.Popen(command.split())


print("\n==== Setup complete! ====")
