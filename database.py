from wsgi import app
from config import *
from flask_sqlalchemy import SQLAlchemy

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

    def __init(self, carName, date, totalMileage, distanceTravelled, gasExpendage, transactionCost, mileageEstimate):
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