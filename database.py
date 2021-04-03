"""
Contains all the models for the database and manage all actions
to and from the PostgresSQL database.
"""

# Imports
from app import api
from config import *
from flask_sqlalchemy import SQLAlchemy

# Define database url
api.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{DATABASE_USERNAME}:{DATABASE_PASSWORD}@{DATABASE_LOCATION}/{DATBASE_NAME}"

pgdb = SQLAlchemy(api)

class FuelEntries(pgdb.Model):
    __tablename__ = "fuel_tracking"
    __table_args__ = {'extend_existing': True}

    carLBL = pgdb.Column(pgdb.String(), nullable=False)
    dateTXN = pgdb.Column(pgdb.String(12), primary_key=True)
    mileageTXN = pgdb.Column(pgdb.Integer(), nullable=False)
    distanceTvlFRMprevENT = pgdb.Column(pgdb.Integer(), nullable=False)
    gasTatTXN = pgdb.Column(pgdb.Float(), nullable=False)
    priceTatTXN = pgdb.Column(pgdb.Float(), nullable=False)
    mpgTXN = pgdb.Column(pgdb.Float(), nullable=False)

    def __init(self, carLBL, dateTXN, mileageTXN, distanceTvlFRMprevENT, gasTatTXN, priceTatTXN, mpgTXN):
        
        self.carLBL = carLBL
        self.dateTXN = dateTXN
        self.mileageTXN = mileageTXN
        self.distanceTvlFRMprevENT = distanceTvlFRMprevENT
        self.gasTatTXN = gasTatTXN
        self.priceTatTXN = priceTatTXN
        self.mileageTXN = mileageTXN
        self.mpgTXN = mpgTXN

class GymSession(pgdb.Model):
    __tablename__ = "gym_tracking"
    __table_args__ = {'extend_existing': True}

    indvNAME = pgdb.Column(pgdb.String(), nullable=False)
    dateSESH = pgdb.Column(pgdb.String(12), primaWry_key=True)
    bodyAtSESH = pgdb.Column(pgdb.String(), nullable=False)
    startSESH = pgdb.Column(pgdb.String(), nullable=False)
    endSESH = pgdb.Column(pgdb.String(), nullable=False)
    calEXP = pgdb.Column(pgdb.Float(), nullable=False)

    def __init(self, indvNAME, dateSESH, bodyAtSESH, startSESH, endSESH, calEXP):
        
        self.indvNAME = indvNAME
        self.dateSESH = dateSESH
        self.bodyAtSESH = bodyAtSESH
        self.startSESH = startSESH
        self.endSESH = endSESH
        self.calEXP = calEXP