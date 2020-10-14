#!/bin/bash
# ------------------------------------------------------------------
# Script starts processes as recommended in:
# https://docs.docker.com/config/containers/multi-service_container/
# ------------------------------------------------------------------

# Start the node exporter
node_exporter --path.rootfs=/host &
status=$?
if [ $status -ne 0 ]; then
  echo "Failed to start node exporter: $status"
  exit $status
fi


#Start the lachesis exporter
lachesis_exporter &
status=$?
if [ $status -ne 0 ]; then
  echo "Failed to start lachesis exporter: $status"
  # exit $status
fi

# Start the grafana server
service grafana-server start &
status=$?
if [ $status -ne 0 ]; then
  echo "Failed to start grafana server: $status"
  # exit $status
fi

# Start the prometheus
prometheus \
--config.file=/etc/prometheus/prometheus.yml \
--storage.tsdb.path=/data &
status=$?
if [ $status -ne 0 ]; then
  echo "Failed to start prometheus: $status"
  # exit $status
fi


# Naive check runs checks once a minute to see if either of the processes exited.
# This illustrates part of the heavy lifting you need to do if you want to run
# more than one service in a container. The container exits with an error
# if it detects that either of the processes has exited.
# Otherwise it loops forever, waking up every 60 seconds
while sleep 60; do
  ps aux |grep node_exporter |grep -q -v grep
  NODE_EXPORTER_STATUS=$?
  ps aux |grep prometheus |grep -q -v grep
  PROMETHEUS_STATUS=$?
  ps aux |grep grafana-server |grep -q -v grep
  GRAFANA_STATUS=$?
  ps aux |grep lachesis_exporter |grep -q -v grep
  LACHESIS_EXPORTER_STATUS=$?

  if [ $NODE_EXPORTER_STATUS -ne 0 ]; then
    echo "Node exporter exited unexpectedly."
  elif [ $PROMETHEUS_STATUS -ne 0 ]; then
    echo "Prometheus exited unexpectedly."
  elif [ $GRAFANA_STATUS -ne 0 ]; then
    echo "Grafana exited unexpectedly."
  elif [ $LACHESIS_EXPORTER_STATUS -ne 0 ]; then
    echo "Lachesis exporter exited unexpectedly."
  fi
done