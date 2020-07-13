import subprocess

print("Initiate Fantom Node Monitor teardown!")

command = "docker network rm monitoring"
subprocess.Popen(command.split())

command = "docker volume rm grafana-volume"
subprocess.Popen(command.split())

command = "docker volume rm influxdb-volume"
subprocess.Popen(command.split())

print("Teardown complete!")