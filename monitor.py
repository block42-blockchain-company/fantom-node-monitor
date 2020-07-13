from common import consts
from influxdb import InfluxDBClient
import datetime


def getTimeStamp():
    return str(datetime.datetime.now().timestamp)

payload = [
    {
        "measurement": consts.TABLE_NAME,
        "fields": {
            "percentage": 0.64,
            "status": "synced"
        }
    }
]


client = InfluxDBClient(host="localhost",
                        port=8086,
                        username=consts.INFLUXDB_ADMIN_USER,
                        password=consts.INFLUXDB_ADMIN_PASSWORD)

client.create_database(consts.DATABASE_NAME)

def getMetric(metric):
    return 1

def storeMetricToDB(db, payload):
    response = client.write_points(payload, database=consts.DATABASE_NAME, protocol='json')
    print(response)


storeMetricToDB(consts.DATABASE_NAME, payload)
