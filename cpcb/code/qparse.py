from email import parser
import re
from datetime import datetime
from datetime import timedelta
import base64
import requests
import sqlite3
import json
import hashlib
import time
import traceback

# db = dataset.connect("sqlite:///../data/db/data.sqlite3")
con = sqlite3.connect('../data/db/data.sqlite3')
cur = con.cursor()
query = "SELECT state, city, site, site_name, query_name, toDate, fromDate, json_data FROM request_status_data WHERE parsed = 0"

# request_status_datatable = db["request_status_data"]
# data_table = db["data"]

# parse_row = request_status_datatable.find_one(parsed=0, status_code=200)
# parse_rows = request_status_datatable.find(parsed=0, status_code=200)

# for i in range(request_status_datatable.__len__()):

for row in cur.execute(query):
  json_data = json.loads(row["json_data"])
  # if data does not exist or has error, skip to next row
  if json_data['status'] == 'failed':
      current_row["parsed"] = 2
      request_status_datatable.update(current_row, ["id"])

        data = json_data["data"]
        tabularData = data["tabularData"]
        bodyContent = tabularData["bodyContent"]

        # if there is no data, skip forward
        if len(bodyContent) < 1:
            print("skipped")
            current_row["parsed"] = 1
            request_status_datatable.update(current_row, ["id"])

        for row in bodyContent:
            insert_row = {}
            insert_row["state"] = current_row["state"]
            insert_row["city"] = current_row["city"]
            insert_row["site"] = current_row["site"]
            insert_row["site_name"] = current_row["site_name"]
            insert_row["query_name"] = current_row["query_name"]

            # dateformat : 14-Oct-2017 - 08:00"
            # print str(row)
            if "to date" in row:
                to_date = row["to date"]
                to_date_array = to_date.split(" - ")
                insert_row["to_date"] = to_date_array[0]
                insert_row["to_time"] = to_date_array[1]

            if "from date" in row:
                from_date = row["from date"]
                from_date_array = from_date.split(" - ")
                insert_row["from_date"] = from_date_array[0]
                insert_row["from_time"] = from_date_array[1]

            if "PM2.5" in row:
                pm25 = row["PM2.5"]
                if pm25 and pm25 != "":
                    insert_row["pm25"] = pm25

            if "PM10" in row:
                pm10 = row["PM10"]
                if pm10 and pm10 != "":
                    insert_row["pm10"] = pm10

            print(insert_row)
            data_table.insert(insert_row)
            # parsed
            current_row["parsed"] = 1

    except Exception:
        traceback.print_exc()
        # error in parsing
        current_row["parsed"] = 2

    # update row to parsed
    request_status_datatable.update(current_row, ["id"])
    db.commit()
