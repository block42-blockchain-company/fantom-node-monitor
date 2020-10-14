import subprocess
from tear_down import *


def setup():
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

    node_monitor_startup = subprocess.run(command.split(), stdout=subprocess.PIPE,
                                          universal_newlines=True, stderr=subprocess.PIPE)

    err_msg = node_monitor_startup.stderr
    if err_msg and "is already in use" in err_msg:
        tear_down()
        setup()


if __name__ == "__main__":
    setup()
