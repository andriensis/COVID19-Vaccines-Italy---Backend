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
    collection.replace_one({"index": regionData["index"]}, data, True)
    if result is None:
        collection.insert_one(data)

url = "https://raw.githubusercontent.com/italia/covid19-opendata-vaccini/master/dati/somministrazioni-vaccini-summary-latest.json"
collection = db.administrationdata
response = urllib.request.urlopen(url)
result = json.loads(response.read())

for administrationData in result['data']:
    data = {
        "index": administrationData["index"],
        "area": administrationData["area"],
        "administration_date": administrationData["data_somministrazione"],
        "total": administrationData["totale"],
        "male": administrationData["sesso_maschile"],
        "female": administrationData["sesso_femminile"],
        "category_health_operators": administrationData["categoria_operatori_sanitari_sociosanitari"],
        "category_not_health_operators": administrationData["categoria_personale_non_sanitario"],
        "category_retirement_homes_guests": administrationData["categoria_ospiti_rsa"],
        "category_age_over_80": administrationData["categoria_over80"],
        "first_dose": administrationData["prima_dose"],
        "second_dose": administrationData["seconda_dose"]
    }
    collection.replace_one({"index": administrationData["index"]}, data, True)
    if result is None:
        collection.insert_one(data)

print("Synchronization completed!")
