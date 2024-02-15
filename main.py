#!/usr/bin/env python
# coding: utf-8
 
# In[4]:


from flask import Flask, jsonify
import os
import psycopg2

# Create flask app variable
app = Flask(__name__)

# Create variables with sign-in details
database = 'gis5572'
user = 'postgres'
password = 'ATLAisagreatshow2020'
host = '35.184.2.25'
port = '5432'

# Create a route to return polygon in GeoJSON format
@app.route('/geojson_polygon')
def get_gj():
    # Connect to DB
    conn = psycopg2.connect(database=database, user=user, password=password, host=host, port=port)
    # Create cursor
    cursor = conn.cursor()

    # Creates GeoJSON string based on polygon stored in PostgreSQL DB
    sql_query = """
    SELECT
        json_build_object(
            "type","FeatureCollection",
            "features",json_agg(
                json_build_object(
                    "type","Feature",
                    "geometry",ST_AsGeoJSON(ST_SetSRID(shape, 4326))::json,
                    "properties",json_build_object()
                )
            ),
            crs,json_build_object(
                "type","name",
                "properties",json_build_object(
                    "name","epsg:4326"
                )
            )
        ) AS geojson
    FROM lab1
    """

    # Gather polygon geojson from above query
    cursor.execute(sql_query)
    gj = cursor.fetchone()[0]

    cursor.close()
    conn.close()

    return gj
    
# Run Flask app
if __name__ == "__main__":
    app.run(
        debug = False,
        host = '0.0.0.0',
        port = int(os.environ.get("PORT", 8080))
    )

