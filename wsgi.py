from flask import Flask, render_template, request, jsonify

app = Flask(__name__, static_url_path='/static')

def throwE(err_code="404"):
    return f"{err_code}"


# Database Imports
from database import *

"""
Take in the car name as an input in the URL
then print out a reply with the data for only
the input.
"""
@app.route('/damocles/v1/<EntryType>/<carNameInput>/<Selection>', methods=['GET'])
def fuel_car_name_all(EntryType, carNameInput, Selection):
    entries = FuelEntry.query.filter_by(carName=carNameInput).all()
    reply = []
    for i in entries:
        entry = {}
        entry["carName"] = i.carName
        entry["date"] = i.date
        entry["totalMileage"] = i.totalMileage
        entry["distanceTravelled"] = i.distanceTravelled
        entry["gasExpendage"] = i.gasExpendage
        entry["transactionCost"] = i.transactionCost
        entry["mileageEstimate"] = i.mileageEstimate
        reply.append(entry)
    if len(reply) == 0:
        reply = throwE()

    return jsonify(reply)

@app.route('/damocles/v1/fuel_entries/all', methods=['GET'])
def call_all_entries():
    allEntries = FuelEntry.query.all()
    out = []
    for i in allEntries:
        entry = {}
        entry["carName"] = i.carName
        entry["date"] = i.date
        entry["totalMileage"] = i.totalMileage
        entry["distanceTravelled"] = i.distanceTravelled
        entry["gasExpendage"] = i.gasExpendage
        entry["transactionCost"] = i.transactionCost
        entry["mileageEstimate"] = i.mileageEstimate
        
        out.append(entry)
    return jsonify(out)

#! Add server side calculations and only take mileage, transactionCost, carName, date and gasExpendage
@app.route('/damocles/v1/fuel_entries/push', methods=['POST'])
def new_entry():
    entryJson = request.get_json()
    entry = FuelEntry(
        carName=entryJson['carName'], 
        date=entryJson['date'],
        totalMileage=entryJson['totalMileage'],
        distanceTravelled=entryJson['distanceTravelled'],
        gasExpendage=entryJson['gasExpendage'],
        transactionCost=entryJson['transactionCost'],
        mileageEstimate=entryJson['mileageEstimate']
        )
    db.session.add(entry)
    db.session.commit()
    return "Posted Entry"

if __name__ == "__main__":
    app.debug = True