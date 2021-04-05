from api.database import database
from sqlalchemy import Column, Integer, String, Float, DateTime
import datetime

class FuelEntry(database.Model):
    __tablename__ = "fuel_entries"
    __tableargs__ = {'extend_existing': True}

    entry_id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(DateTime, default=datetime.datetime.utcnow)
    carName = Column(String, nullable=False)
    mileage = Column(Integer, nullable=False)
    distanceTravelledBetweenEntry = Column(Integer, nullable=False)
    gasTotal = Column(Float, nullable=False)
    priceTotal = Column(Float, nullable=False)
    MPG = Column(Float, nullable=False)

    def __init(self, date, carName, mileage, distanceTravelledBetweenEntry, gasTotal, priceTotal, MPG):

        self.date = date
        self.carName = carName
        self.mileage = mileage
        self.distanceTravelledBetweenEntry = distanceTravelledBetweenEntry
        self.gasTotal = gasTotal
        self.priceTotal = priceTotal
        self.mileage = mileage
        self.MPG = MPG

class GymEntry(database.Model):
    __tablename__ = "gym_entries"
    __tableargs__ = {'extend_existing': True}

    entry_id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(DateTime, default=datetime.datetime.utcnow)
    individualName = Column(String, nullable=False)
    bodyPhotoABS = Column(String, nullable=False)
    individualWeight = Column(Float, nullable=False)
    startTime = Column(DateTime, nullable=False)
    endTime = Column(DateTime, nullable=False)
    caloriesExpended = Column(Float, nullable=False)

    def __init(self, date, individualName, bodyPhotoABS, individualWeight, startTime, endTime, caloriesExpended):
        
        self.date = date
        self.individualName = individualName
        self.bodyPhotoABS = bodyPhotoABS
        self.individualWeight = individualWeight
        self.startTime = startTime
        self.endTime = endTime
        self.caloriesExpended = caloriesExpended
