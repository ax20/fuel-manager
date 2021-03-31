from flask import Flask, render_template, request, jsonify
from config import *
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__, static_url_path='/static')

app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{DATABASE_USERNAME}:{DATABASE_PASSWORD}@{DATABASE_LOCATION}/{DATBASE_NAME}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class FuelEntry(db.Model):
    __tablename__ = "fuel_entries"
    __table_args__ = {'extend_existing': True}

    carName = db.Column(db.String(100), primary_key=True)
    date = db.Column(db.String(12), nullable=False)
    totalMileage = db.Column(db.Integer(), nullable=False)
    distanceTravelled = db.Column(db.Integer(), nullable=False)
    gasExpendage = db.Column(db.Float(), nullable=False)
    transactionCost = db.Column(db.Float(), nullable=False)
    mileageEstimate = db.Column(db.Float(), nullable=False)

    def __init(self, carName, date, totalMileage, distanceTravelled, gasExpendage, transactionCost):
        self.carName = carName
        self.date = date
        self.totalMileage = totalMileage
        self.distanceTravelled = distanceTravelled
        self.gasExpendage = gasExpendage
        self.transactionCost = transactionCost
        self.mileageEstimate = mileageEstimate
        
class GymEntry(db.Model):
    __tablename__ = "gym_entries"
    __table_args__ = {'extend_existing': True}

    individualName = db.Column(db.String(100), primary_key=True)
    date = db.Column(db.String(12), nullable=False)
    bodyPicture = db.Column(db.String(), nullable=False)
    startTime = db.Column(db.String(), nullable=False)
    endTime = db.Column(db.String(), nullable=False)
    caloriesBurnt = db.Column(db.Float(), nullable=False)

    def __init(self, individualName, date, bodyPicture, startTime, endTime, caloriesBurnt):
        self.individualName = individualName
        self.date = date
        self.bodyPicture = bodyPicture
        self.startTime = startTime
        self.endTime = endTime
        self.caloriesBurnt = caloriesBurnt

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