"""
    This script will go through CSVs to find the heaviest payload
    that we are able to see a truck type carrying. 
    This will help us gain insight into the maximum capacities of each
    truck type
"""
import csv
import datetime

type_capacity_dict = {}

for i in range(69):
    with open(f"/home/justin/Desktop/BCIT Share/repos/QDpieS/truck_data/truck{i}.csv") as file:
        csvreader = csv.reader(file)

        for i, row in enumerate(csvreader):
            type = row[8]
            payload = row[4]

            if type not in type_capacity_dict.keys():
                type_capacity_dict[type] = payload
                continue
            elif payload > type_capacity_dict[type]:
                type_capacity_dict[type] = payload

print(type_capacity_dict)