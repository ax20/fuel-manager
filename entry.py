
 
database import pgdb, FuelEntries, GymSession
from flask import jsonify
from config import ADMIN_TOKEN

def get_all_entries(type, selector):
    reply = []

    if type == "fuel":
        entries = FuelEntries.query.filter_by(carLBL=selector).all()
        
        for entry in entries:
            item = {
                "carLBL": entry.carLBL,
                "dateTXN": entry.dateTXN,
                "mileageTXN": entry.mileageTXN,
                "distanceTvlFRMprevENT": entry.distanceTvlFRMprevENT,
                "gasTatTXN": entry.gasTatTXN,
                "priceTatTXN": entry.priceTatTXN,
                "mpgTXN": entry.mpgTXN
            }
            reply.append(item)
    
    elif type == "gym":
        entries = GymSession.query.filter_by(indvNAME=selector).all()
        
        for entry in entries:
            item = {
                "indvNAME": entry.indvNAME,
                "dateSESH": entry.dateSESH,
                "bodyAtSESH": entry.bodyAtSESH,
                "startSESH": entry.startSESH,
                "endSESH": entry.endSESH,
                "calEXP": entry.calEXP
            }
            reply.append(item)

    if len(reply) == 0:
        return "404, how tf do you not know your own api?"
    
    return reply

def push_entry(type, selector, json):

    data = json

    if data.get('secret') == None or data.get('secret') != ADMIN_TOKEN:
        return "200, go fuck yourself"

    if type == "fuel":
        item = FuelEntries(
             carLBL = selector,
             dateTXN = data['dateTXN'],
             mileageTXN = data['mileageTXN'],
             distanceTvlFRMprevENT = data['distanceTvlFRMprevENT'],
             gasTatTXN = data['gasTatTXN'],
             priceTatTXN = data['priceTatTXN'],
             mpgTXN = data['mpgTXN']
        )

    elif type == "gym":
        item = GymSession(
             indvNAME = selector,
             dateSESH = data['dateSESH'],
             bodyAtSESH = data['bodyAtSESH'],
             startSESH = data['startSESH'],
             endSESH = data['endSESH'],
             calEXP = data['calEXP']
        )

    pgdb.session.add(item)
    pgdb.session.commit()

    return "200, posted gang"