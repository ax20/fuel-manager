"""
handle all transactions with database
"""
from api.config import *
from app import api
from flask_sqlalchemy import SQLAlchemy

api.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{DATABASE_USERNAME}:{DATABASE_PASSWORD}@{DATABASE_LOCATION}/{DATBASE_NAME}"
database = SQLAlchemy(api)


def new_entry(model):
    database.session.add(model)
    database.commit()

def create_all_tables():
    from api.data_models import *
    database.create_all()

# https://stackoverflow.com/a/13065584/9254757
def drop_all_tables():
    import psycopg2, sys
    try:
    conn = psycopg2.connect(f"dbname='{DATBASE_NAME}' user='{DATABASE_USERNAME}' password='{DATABASE_PASSWORD}'")
    conn.set_isolation_level(0)
    except:
        print "Unable to connect to the database."

    cur = conn.cursor()

    try:
        cur.execute("SELECT table_schema,table_name FROM information_schema.tables WHERE table_schema = 'public' ORDER BY table_schema,table_name")
        rows = cur.fetchall()
        for row in rows:
            print "dropping table: ", row[1]   
            cur.execute("drop table " + row[1] + " cascade") 
        cur.close()
        conn.close()        
    except:
        print "Error: ", sys.exc_info()[1]