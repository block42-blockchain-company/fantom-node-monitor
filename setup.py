import subprocess
from tear_down import *


def setup():
    try:
        print("==== Fantom Node Monitor Setup ====\n")

        print("Create persistent volumes:")

        command = "docker volume create prometheus-volume"
        prometheus_volume_creation = subprocess.Popen(command.split())

        prometheus_volume_creation.wait()

        print("Start container")

        # "host" attributes necessary in order for node_exporter to access host machine metrics
        command = 'docker run -d \
          --net=host \
          --pid=host \
          -v /:/host:ro,rslave \
          -v prometheus-volume:/data \
          --name fantom-node-monitor \
          block42blockchaincompany/fantom-node-monitor'

        node_monitor_startup = subprocess.run(command.split())
        node_monitor_startup.check_returncode()
    except subprocess.CalledProcessError as e:
        print(e.output)
        tear_down()
        setup()


if __name__ == "__main__":
    setup()
