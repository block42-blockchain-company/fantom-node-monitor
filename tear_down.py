import subprocess
import os
import signal
from common import consts


print("==== Fantom Node Monitor Teardown ====\n")

command = "docker-compose down"
shutdown_container = subprocess.Popen(command.split())
shutdown_container.wait()

command = "lsof -ti :{}".format(consts.NODE_EXPORTER_PORT)
shutdown_node_exporter = subprocess.Popen(command.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)

stdout, stderr = shutdown_node_exporter.communicate()
print(stdout.decode("utf-8"))
for process in str(stdout.decode("utf-8")).split("\n")[1:]:
    data = [x for x in process.split(" ") if x != '']
    if len(data) > 1:
        print("Killing {}".format(data))
        os.kill(int(data[1]), signal.SIGKILL)

command = "docker volume rm grafana-volume"
rm_grafana_volume = subprocess.Popen(command.split())

command = "docker volume rm prometheus-volume"
rm_prometheus_volume = subprocess.Popen(command.split())

rm_grafana_volume.wait()
rm_prometheus_volume.wait()
shutdown_node_exporter.wait()

# TODO: Shut down Node_Exporter!

print("Teardown complete!")
