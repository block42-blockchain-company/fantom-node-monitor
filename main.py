import argparse
import subprocess
import sys


def setup():
    print("==== Fantom Node Monitor Setup ====")

    print("Create persistent volumes:")

    command = "docker volume create prometheus-volume"
    prometheus_volume_creation = subprocess.Popen(command.split())

    prometheus_volume_creation.wait()

    print("Start container\n")

    # "host" attributes necessary in order for node_exporter to access host machine metrics
    command = 'docker run -d \
      --net=host \
      --pid=host \
      -v /:/host:ro,rslave \
      -v prometheus-volume:/data \
      --name fantom-node-monitor \
      block42blockchaincompany/fantom-node-monitor'

    node_monitor_startup = subprocess.run(command.split(), stdout=subprocess.PIPE,
                                          universal_newlines=True, stderr=subprocess.PIPE)

    err_msg = node_monitor_startup.stderr
    if err_msg and "is already in use" in err_msg:
        tear_down()
        setup()


def tear_down():
    print("==== Fantom Node Monitor Teardown ====")

    command = "docker rm -f fantom-node-monitor"
    rm_container = subprocess.Popen(command.split())
    rm_container.wait()

    command = "docker volume rm prometheus-volume"
    rm_prometheus_volume = subprocess.Popen(command.split())
    rm_prometheus_volume.wait()

    print("Teardown complete!\n")


def build():
    command = "docker build -t block42blockchaincompany/fantom-node-monitor ."
    node_monitor_startup = subprocess.Popen(command.split())
    node_monitor_startup.wait()


def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='command', title='command')
    subparsers.required = True
    subparsers.add_parser('setup', help='Start your docker container to monitor your fantom node.')
    subparsers.add_parser('teardown', help='Stop monitoring fantom node and clean-up.')
    subparsers.add_parser('build', help='Build a new docker image from source.')

    args = parser.parse_args()
    if args.command == "setup":
        setup()
    elif args.command == "teardown":
        tear_down()
    elif args.command == "build":
        build()


if __name__ == "__main__":
    sys.exit(main())
