from common import consts
from influxdb import InfluxDBClient

# For very basic testing only
# Inserts a single datapoint into the db

client = InfluxDBClient(host="localhost",
                        port=8086,
                        username=consts.INFLUXDB_ADMIN_USER,
                        password=consts.INFLUXDB_ADMIN_PASSWORD)

def getMetric():
    return [{
        "measurement": consts.TABLE_NAME,
        "fields": {
            "percentage": 0.64,
            "status": "synced"
        }
    }]

def storeMetricToDB(db, payload):
    client.write_points(payload, database=consts.DATABASE_NAME, protocol='json')


storeMetricToDB(consts.DATABASE_NAME, getMetric())
