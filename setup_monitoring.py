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

command = '/usr/share/grafana/conf/provisioning/datasources'

# TODO 
#     - replace USER_NAME and USER_PASSWORD in datasource_template.yaml
#     - store substituted version in container grafana at /usr/share/grafana/conf/provisioning/datasources 
#     - check out how to create dashboard graph automatically 

# Next steps:
#     - maybe use memory usage as first metric#     
#           - use python to query data from lachesis api (dunno anything about api yet)
#     - use telegraf as input method for influxdb 
