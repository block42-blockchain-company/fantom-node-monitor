import subprocess

print("==== Fantom Node Monitor Teardown ====\n")

command = "docker-compose down"
shutdown = subprocess.Popen(command.split())
shutdown.wait()

command = "docker network rm monitoring"
rm_network = subprocess.Popen(command.split())

command = "docker volume rm grafana-volume"
rm_grafana_volume = subprocess.Popen(command.split())

command = "docker volume rm prometheus-volume"
rm_prometheus_volume = subprocess.Popen(command.split())

rm_network.wait()
rm_grafana_volume.wait()
rm_prometheus_volume.wait()

# TODO: Shut down Node_Exporter!

print("Teardown complete!")
