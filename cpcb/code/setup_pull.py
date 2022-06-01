import re
from datetime import datetime
from datetime import timedelta
import base64
import requests
import dataset
import json
import hashlib
import time

def create_params_query(params_list):
    # '[{"id":0,"itemName":"PM2.5","itemValue":"parameter_193"},{"id":1,"itemName":"PM10","itemValue":"parameter_215"}'
    result = []
    for i in range(len(params_list)):
        param_dict = {"id": i}
        param_dict['itemName'] = params_list[i]
        param_dict['itemValue'] = PARAMS_MAP[params_list[i]]
        result.append(param_dict)
    result = str(result)
    result = result.replace("'", '"')
    result = result.replace('", "', '","')
    return result

def give_params_ids(params_list):
    # '["parameter_193","parameter_215"]'
    result = []
    for i in params_list:
        result.append(PARAMS_MAP[i])
    result = str(result)
    result = result.replace("'", '"')
    return result

PARAMS_MAP = {"PM2.5": "parameter_193", "PM10": "parameter_215", "NO": "parameter_226", "NO2": "parameter_194", "NOx": "parameter_225", "NH3": "parameter_311", "SO2": "parameter_312", "CO": "parameter_203", "Ozone": "parameter_222", "Benzene": "parameter_202", "Toluene": "parameter_232", "Eth-Benzene": "parameter_216", "MP-Xylene": "parameter_240", "RH": "parameter_235", "WD": "parameter_234", "SR": "parameter_237", "BP": "parameter_238", "AT": "parameter_204", "TOT-RF": "parameter_37", "RF": "parameter_236", "Xylene": "parameter_223", "WS": "parameter_233", "O Xylene": "parameter_241", "Temp": "parameter_198", "VWS": "parameter_239", "P-Xylene": "parameter_324", "Rack Temp": "parameter_218"}

db = dataset.connect("sqlite:///../data/db/data.sqlite3")
# TODO 1: edit data/db/data.sqlite3 and add the sites you want to scrape into sites table
site_table = db["file"]
run_name = "run2_"  # leave this as it is

for site_row in site_table:
    state = site_row["state"]
    city = site_row["city"]
    site = site_row["site"]
    site_name = site_row["site_name"]
    params_list = site_row["params"].strip("]['").split(", ") # converts str of list back to list because we want string quotes on elements
    params_query = site_row["params_query"]
    params_ids = site_row["params_ids"]

    label = (
        state.lower().replace(" ", "")
        + "_"
        + city.lower().replace(" ", "-")
        + "_"
        + site
        + "_"
    )
    table = db["request_status_data"]

    fromDate = "01-01-2010"  # TODO 2: starting date (inclusive)
    endDate = "31-12-2015"  # TODO 3: ending date (inclusive)
    how_many_days = 1

    toDate = ""
    objFromDate = datetime.strptime(fromDate, "%d-%m-%Y")
    time_part = " T00:00:00Z"
    time_part_end = " T00:00:01Z"
    status_code = 1

    print(site_name)
    while objFromDate <= datetime.strptime(endDate, "%d-%m-%Y"):
        # print("####################################################")

        objToDate = objFromDate + timedelta(days=how_many_days)

        fromDate = objFromDate.strftime("%d-%m-%Y") + time_part
        toDate = objToDate.strftime("%d-%m-%Y") + time_part_end

        query_name = run_name + label + objFromDate.strftime("%Y%m%d")
        # print(query_name)
        
        # print(fromDate + " – " + toDate)

        # row_exists = table.find_one(query_name=query_name) ## this query slows the code
        # if row_exists:
        #     objFromDate = objToDate
        #     # print("EXISTS SO GO TO NEXT")
        #     continue

        prompt_all = (
            '{"draw":1,"columns":[{"data":0,"name":"","searchable":true,"orderable":false,"search":{"value":"","regex":false}}],"order":[],"start":0,"length":10,"search":{"value":"","regex":false},"filtersToApply":{"parameter_list":'
            + params_query
            + ',"criteria":"24 Hours","reportFormat":"Tabular","fromDate":"'
            + fromDate
            + '","toDate":"'
            + toDate
            + '","state":"'
            + state
            + '","city":"'
            + city
            + '","station":"'
            + site
            + '","parameter":'
            + params_ids
            + ',"parameterNames":'
            + str(params_list).replace("'", '"') # need double quotes for it to work
            + '},"pagination":1}'
        )

        data_to_encode = prompt_all
        encoded_data = base64.b64encode(data_to_encode.encode("UTF8"))
        # print(data_to_encode)

        row = {}
        row["query_name"] = query_name
        row["fromDate"] = fromDate
        row["toDate"] = toDate
        row["state"] = state
        row["city"] = city
        row["site"] = site
        row["site_name"] = site_name
        row["data_to_encode"] = data_to_encode
        row["encoded_data"] = encoded_data
        row["status_code"] = status_code
        row["parsed"] = 0
        table.insert(row)

        # forward in date for next
        objFromDate = objToDate
        # print("_______________________________________________________________")
        # end while
