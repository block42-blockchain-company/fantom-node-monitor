# Fantom Node Monitor

## Getting started

### Prerequists
Make sure that the package manager for python3 is installed. You can do that via

```    
sudo apt-get install python3-pip
```
Make sure all dependenices are installed:

```
pip3 install -r requirements.txt
```

### Setup

Start the monitor with the following command:
```shell
python3 ./setup.py
```

You can view the dashboard by accessing the machine on port 3000.


### Tear Down
*Note: Be aware that the following will also remove all data collected!*
Stop the containers and remove all artifcats with:
```shell
python3 ./tear_down.py
```


