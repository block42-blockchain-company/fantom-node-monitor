import requests
from common import consts


def getMetric(metric):

    return 1

def storeMetricToDB(db, payload):
    response = requests.post(consts.DATABASE_URL + "write?db={}".format(db), payload)
    print(response.text)


insert_payload = consts.TABLE_NAME + "," + "value=0.20"
storeMetricToDB(consts.DATABASE_NAME, insert_payload)
