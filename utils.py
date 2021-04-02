import json, config
from datetime import datetime


def log(x):
    time = datetime.now().strftime("(%H:%M:%S)")
    date = datetime.now().strftime("%Y-%m-%d")
    file = config.LOG_FILE + "_" + date
    with open(file, 'a') as log:
        log.write(f"{time} => {x}")

def calculate_mileage(distance_travelled, gas_expendage):
    return round(distance_travelled/gas_expendage, 2)

def calculate_distance_travelled(mileage_current):
    mileage_previous = get_objects_from_latest_entry("mileage")
    return (mileage_current-mileage_previous)

def update_latest_entry(json):
    with open(config.LATEST_ENTRY_FILE, 'w') as latest:
        latest.write(json)
        latest.close()
    
def get_objects_from_latest_entry(object):
    x = []
    with open(config.LATEST_ENTRY_FILE, 'r') as latest:
        x.append(latest.read())
        latest.close()
    return x[0][object]

def build_entry_post(EntryType, json):
    if EntryType == "fuel":
        mileage = json["mileage"]
        gasExpendage = json["gasExpendage"]
        transactionCost = json["transactionCost"]
        
        