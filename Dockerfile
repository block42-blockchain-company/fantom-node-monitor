FROM ubuntu:18.04

RUN mkdir /node-monitor

RUN apt-get update
RUN apt-get install -y python3.7
RUN apt-get install -y golang-go

ADD setup.py /node-monitor/
ADD grafana /node-monitor/
ADD prometheus /node-monitor/
ADD exporter/lachesis_exporter /node-monitor

CMD [ "python3", "./node-monitor/setup.py" ]
