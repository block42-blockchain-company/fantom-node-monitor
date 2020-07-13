from common import consts
from influxdb import InfluxDBClient


client = InfluxDBClient(host="localhost",
                        port=8086,
                        username=consts.INFLUXDB_ADMIN_USER,
                        password=consts.INFLUXDB_ADMIN_PASSWORD)

client.create_database(consts.DATABASE_NAME)

def getMetric(metric):

    return 1

def storeMetricToDB(db, payload):
    response = client.write_points(payload, database=consts.DATABASE_NAME, protocol='line')
    print(response)


insert_payload = consts.TABLE_NAME + "," + "value=0.20"
storeMetricToDB(consts.DATABASE_NAME, insert_payload)
