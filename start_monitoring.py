import subprocess

ADMIN_USER="admin"
ADMIN_PASSWORD="admin123"

command = "docker network create monitoring"
subprocess.Popen(command.split())

command = "docker volume create grafana-volume"
subprocess.Popen(command.split())

command = "docker volume create influxdb-volume"
subprocess.Popen(command.split())

command = '''docker run --rm -e INFLUXDB_HTTP_AUTH_ENABLED=true \
         -e INFLUXDB_ADMIN_USER={} \
         -e INFLUXDB_ADMIN_PASSWORD={} \
         -v /var/lib/influxdb:/var/lib/influxdb \
         -v /etc/influxdb/scripts:/docker-entrypoint-initdb.d \
         influxdb /init-influxdb.sh '''.format(ADMIN_USER, ADMIN_PASSWORD)
subprocess.Popen(command.split())

command = 'docker-compose up -d'
subprocess.Popen(command.split())


