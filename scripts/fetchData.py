import urllib.request
import json
from enum import Enum
from pymongo import MongoClient

client = MongoClient(
    "mongodb://admin:Covid19Vaccini@covid19-vaccines-mongo:27017/covid19vaccines?authSource=admin&w=1")
db = client.covid19vaccines
collection = db.latestdata

url = "https://raw.githubusercontent.com/italia/covid19-opendata-vaccini/master/dati/vaccini-summary-latest.json"
response = urllib.request.urlopen(url)
result = json.loads(response.read())

for regionData in result['data']:
    data = {
        "index": regionData["index"],
        "area": regionData["area"],
        "doses_administered": regionData["dosi_somministrate"],
        "doses_delivered": regionData["dosi_consegnate"],
        "administration_percentage": regionData["percentuale_somministrazione"],
        "last_update": regionData["ultimo_aggiornamento"]
    }
    print(data)
    collection.replace_one({"index": regionData["index"]}, data, True)
    if result is None:
        collection.insert_one(data)
