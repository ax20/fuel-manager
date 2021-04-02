from flask import Flask, render_template, request, jsonify

app = Flask(__name__, static_url_path='/static')

def throwE(err_code="404"):
    return f"{err_code}"

# Database Imports
from database import *
from utils import build_entry_post, log
"""
Take in the car name as an input in the URL
then print out a reply with the data for only
the input.
"""
@app.route('damocles/v1/<EntryType>/<SelectionInput>/all', methods=['GET'])
def fuel_car_name_all(EntryType, SelectionInput):
    reply = []
    log(f"GET {EntryType}, {SelectionInput}")
    if EntryType == "fuel":
        entries = FuelEntry.query.filter_by(carName=SelectionInput).all()
        for input in entries:
            entry = {}
            entry["carName"] = input.carName
            entry["date"] = input.date
            entry["totalMileage"] = input.totalMileage
            entry["distanceTravelled"] = input.distanceTravelled
            entry["gasExpendage"] = input.gasExpendage
            entry["transactionCost"] = input.transactionCost
            entry["mileageEstimate"] = input.mileageEstimate
            reply.append(entry)

    elif EntryType == "gym":
        entries = GymEntry.query.filter_by(individualName=SelectionInput).all()
        for input in entries:
            entry = {}
            entry["individualName"] = input.individualName
            entry["date"] = input.date
            entry["bodyPicture"] = input.bodyPicture
            entry["startTime"] = input.startTime
            entry["endTime"] = input.endTime
            entry["caloriesBurnt"] = input.caloriesBurnt
            reply.append(entry)
    
    if len(reply) == 0:
        return throwE()

    return jsonify(reply)

#! Add server side calculations and only take mileage, transactionCost, carName, date and gasExpendage
@app.route('/v1/<EntryType>', methods=['POST'])
def new_entry(EntryType):

    if EntryType == "fuel":
        entry= FuelEntry(
            carName=entryJson['carName'], 
            date=entryJson['date'],
            totalMileage=entryJson['totalMileage'],
            distanceTravelled=entryJson['distanceTravelled'],
            gasExpendage=entryJson['gasExpendage'],
            transactionCost=entryJson['transactionCost'],
            mileageEstimate=entryJson['mileageEstimate']
            )
        
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