import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import datetime as dt

from flask import Flask, jsonify

# create engine
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(autoload_with=engine)
Base.classes.keys()

# Save references to each table
Station = Base.classes.station
Measurement = Base.classes.measurement

#flask setup
app = Flask(__name__)

#Flask routes

@app.route("/")
def welcome():
    return (
        f"Hello...Welcome to Honolulu,Hawaii...!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/yyyy-mm-dd<br/>"
        f"/api/v1.0/2010-09-20/2015-05-28"
    )

@app.route("/api/v1.0/precipitation")
def prcp():
    session = Session(engine)
    prcp_result = session.query(Measurement.date,Measurement.prcp).all()
    session.close()
# create dictionary
    all_precipitation = []
    for date, prcp in prcp_result:
        all_precipitation_dict = {}
        all_precipitation_dict["date"] = date
        all_precipitation_dict["prcp"] = prcp
        all_precipitation.append(all_precipitation_dict)

    return jsonify(all_precipitation)


@app.route("/api/v1.0/stations")
def station():
    session = Session(engine)
    station_result = session.query(Measurement.station).all()
    session.close()
    all_station = list(np.ravel(station_result))
    return jsonify(all_station)


@app.route("/api/v1.0/tobs")
def tobs():
    session = Session(engine)
    date_oneyear_ago = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    active_station_temp = session.query(Measurement.date, Measurement.tobs).filter(Measurement.station == 'USC00519281').filter(Measurement.date >= date_oneyear_ago).all()
    session.close()
# create dictionary
    active_station_temparature = []
    for date, tobs in active_station_temp:
        active_station_temp_dict = {}
        active_station_temp_dict["date"] = date
        active_station_temp_dict["tobs"] = tobs
        active_station_temparature.append(active_station_temp_dict)

    return jsonify(active_station_temparature)


@app.route("/api/v1.0/<start>")
def start(start):
    session = Session(engine)
    temp_summary1 = session.query(func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)).filter(Measurement.date >= start).all()
    session.close()
# create dictionary
    summary1 = []
    for min, max, avg in temp_summary1:
        summary_dict1 = {}
        summary_dict1["TMIN"] = min
        summary_dict1["TMAX"] = max
        summary_dict1["TAVG"] = avg
        summary1.append(summary_dict1)

        if summary_dict1["TMIN"]:
             return jsonify(summary1)  
        
    return jsonify({"error": f"Date {start} not found."}), 404


@app.route("/api/v1.0/<start>/<end>")
def startend(start,end):
    session = Session(engine)
    temp_summary2 = session.query(func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)).\
        filter(Measurement.date >= start).filter(Measurement.date <= end).all()
    session.close()
#create dictionary
    summary2 = []
    for min, max, avg in temp_summary2:
        summary_dict2 = {}
        summary_dict2["TMIN"] = min
        summary_dict2["TMAX"] = max
        summary_dict2["TAVG"] = avg
        summary2.append(summary_dict2)

        if summary_dict2["TMIN"]:
            return jsonify(summary2)
        
    return jsonify({"error": f"Invalid Data Range."}), 404
   

if __name__ == '__main__':
    app.run(debug=True)
