import subprocess
from resources.common import consts

print("==== Fantom Node Monitor Teardown ====\n")

command = "docker rm -f fantom-node-monitor"
rm_container = subprocess.Popen(command.split())
rm_container.wait()

command = "docker volume rm prometheus-volume"
rm_prometheus_volume = subprocess.Popen(command.split())
rm_prometheus_volume.wait()

print("Teardown complete!")
