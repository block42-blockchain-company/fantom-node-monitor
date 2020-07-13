import subprocess
from influxdb import InfluxDBClient
from common import consts

print("==== Fantom Node Monitor Setup ====\n")

command = "docker network create monitoring"
network_setup = subprocess.Popen(command.split())

command = "docker volume create grafana-volume"
grafana_volume_creation = subprocess.Popen(command.split())

command = "docker volume create influxdb-volume"
influxdb_volume_creation = subprocess.Popen(command.split())

grafana_volume_creation.wait()
network_setup.wait()
influxdb_volume_creation.wait()


print("\n==== Initialize InfluxDB ====")
command = '''docker run --rm -e INFLUXDB_HTTP_AUTH_ENABLED=true \
         -e INFLUXDB_ADMIN_USER={} \
         -e INFLUXDB_ADMIN_PASSWORD={} \
         -v /var/lib/influxdb:/var/lib/influxdb \
         -v /etc/influxdb/scripts:/docker-entrypoint-initdb.d \
         influxdb /init-influxdb.sh '''.format(consts.INFLUXDB_ADMIN_USER, consts.INFLUXDB_ADMIN_PASSWORD)
init_influxdb = subprocess.Popen(command.split())
init_influxdb.wait()


print("\n==== Start Grafana and InfluxDB Container ====")
command = 'docker-compose up -d'
spin_up_containers = subprocess.Popen(command.split())
spin_up_containers.wait()


print("\n==== Create Database ====")
client = InfluxDBClient(host="localhost",
                        port=8086,
                        username=consts.INFLUXDB_ADMIN_USER,
                        password=consts.INFLUXDB_ADMIN_PASSWORD)
client.create_database(consts.DATABASE_NAME)


print("\n==== Start Monitoring Service ====")
# Note: the script below is only for basic testing and has nothing to do with the actual monitoring!
command = "python3 ./monitor.py"
create_db = subprocess.Popen(command.split())


print("\n==== Setup complete! ====")
