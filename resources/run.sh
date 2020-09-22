#!/bin/bash

# Start the node exporter
node_exporter --path.rootfs=/host &
status=$?
if [ $status -ne 0 ]; then
  echo "Failed to start my_first_process: $status"
  exit $status
fi


#Start the lachesis exporter
lachesis_exporter &
status=$?
if [ $status -ne 0 ]; then
  echo "Failed to start my_second_process: $status"
  # exit $status
fi

# Start the grafana server
service grafana-server start &
status=$?
if [ $status -ne 0 ]; then
  echo "Failed to start my_second_process: $status"
  # exit $status
fi

# Start the prometheus
prometheus \
--config.file=/etc/prometheus/prometheus.yml \
--storage.tsdb.path=/data &
status=$?
if [ $status -ne 0 ]; then
  echo "Failed to start my_second_process: $status"
  # exit $status
fi


# Naive check runs checks once a minute to see if either of the processes exited.
# This illustrates part of the heavy lifting you need to do if you want to run
# more than one service in a container. The container exits with an error
# if it detects that either of the processes has exited.
# Otherwise it loops forever, waking up every 60 seconds

while sleep 30; do
  ps aux |grep node_exporter |grep -q -v grep
  NODE_EXPORTER_STATUS=$?
  ps aux |grep prometheus |grep -q -v grep
  PROMETHEUS_STATUS=$?
  ps aux |grep grafana-server |grep -q -v grep
  GRAFANA_STATUS=$?
  ps aux |grep lachesis_exporter |grep -q -v grep
  LACHESIS_EXPORTER_STATUS=$?
  echo "Node_exporter: $NODE_EXPORTER_STATUS"
  echo "Prometheus: $PROMETHEUS_STATUS"
  echo "Grafana: $GRAFANA_STATUS"
  echo "Lachesis: $LACHESIS_EXPORTER_STATUS"
  # If the greps above find anything, they exit with 0 status
  # If they are not both 0, then something is wrong
  if [ $NODE_EXPORTER_STATUS -ne 0 -o $LACHESIS_EXPORTER_STATUS -ne 0 ] ||
     [ $GRAFANA_STATUS -ne 0 -o $PROMETHEUS_STATUS -ne 0 ]; then
    echo "One of the processes has already exited."
    exit 1
  fi
done