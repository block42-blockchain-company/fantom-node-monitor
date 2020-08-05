import subprocess
from common import consts

def shutDownProcessByPort(port):
    command = "lsof -ti :{}".format(port)
    shutdown_node_exporter = subprocess.Popen(command.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = shutdown_node_exporter.communicate()
    pid = stdout.decode("utf-8")
    print(pid)

    command = "kill {}".format(pid)
    subprocess.Popen(command.split())


print("==== Fantom Node Monitor Teardown ====\n")

command = "docker-compose down"
shutdown_container = subprocess.Popen(command.split())
shutdown_container.wait()

command = "docker volume rm grafana-volume"
rm_grafana_volume = subprocess.Popen(command.split())

command = "docker volume rm prometheus-volume"
rm_prometheus_volume = subprocess.Popen(command.split())

command = "docker stop node_exporter"
shutDownProcessByPort(consts.LACHESIS_EXPORTER_PORT)

rm_grafana_volume.wait()
rm_prometheus_volume.wait()

print("Teardown complete!")
