#!/bin/bash

# Start the node exporter
node_exporter --path.rootfs=/host &
status=$?
if [ $status -ne 0 ]; then
  echo "Failed to start my_first_process: $status"
  exit $status
fi


# Start the lachesis exporter
#lachesis_exporter &
#status=$?
#echo "Status", $status
#if [ $status -ne 0 ]; then
#  echo "Failed to start my_second_process: $status"
#  # exit $status
#fi

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

while sleep 5; do
  ps aux |grep node_exporter |grep -q -v grep
  PROCESS_1_STATUS=$?
  ps aux |grep prometheus |grep -q -v grep
  PROCESS_2_STATUS=$?
  ps aux |grep grafana-server |grep -q -v grep
  PROCESS_3_STATUS=$?
  echo "Node_exporter: $PROCESS_1_STATUS"
  echo "prometheus: $PROCESS_2_STATUS"
  echo "grafana: $PROCESS_3_STATUS"
  # If the greps above find anything, they exit with 0 status
  # If they are not both 0, then something is wrong
  if [ $PROCESS_1_STATUS -ne 0 -o $PROCESS_2_STATUS -ne 0 ]; then
    echo "One of the processes has already exited."
    exit 1
  fi
done