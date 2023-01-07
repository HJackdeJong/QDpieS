import json
import csv

count = 0
timestamp = ["" for a in range(100002)]
north = ["" for a in range(100002)]
east = ["" for a in range(100002)]
elev = ["" for a in range(100002)]
status = ["" for a in range(100002)]
payload = ["" for a in range(100002)]
fuelRate = ["" for a in range(100002)]
truckId = ["" for a in range(100002)]
typeId = ["" for a in range(100002)]
shovelId = ["" for a in range(100002)]
dumpId = ["" for a in range(100002)]

for i in range(10):
    with open(f"C:\\Users\\kalel\\OneDrive\\Desktop\\data_group{i}.json", 'r') as file:
        data = json.load(file)

    # print(len(data['TIMESTAMP']), end=" | ")
    # print(len(data['GPSNORTHING']), end=" | ")
    # print(len(data['GPSEASTING']), end=" | ")
    # print(len(data['GPSELEVATION']), end=" | ")
    # print(len(data['FUEL_RATE']), end=" | ")
    # print(len(data['STATUS']), end=" | ")
    # print(len(data['PAYLOAD']), end=" | ")
    # print(len(data['TRUCK_ID']), end=" | ")
    # print(len(data['TRUCK_TYPE_ID']), end=" | ")
    # print(len(data['SHOVEL_ID']), end=" | ")
    # print(len(data['DUMP_ID']))  


    for i in range(100000):
        if str(i) in data['TIMESTAMP']:
            timestamp[i] = data['TIMESTAMP'][str(i)];
            north[i] = data['GPSNORTHING'][str(i)];
            east[i] = data['GPSEASTING'][str(i)];
            elev[i] = data['GPSELEVATION'][str(i)];
            fuelRate[i] = data['FUEL_RATE'][str(i)];
            status[i] = data['STATUS'][str(i)];
            payload[i] = data['PAYLOAD'][str(i)];
            truckId[i] = data['TRUCK_ID'][str(i)];
            typeId[i] = data['TRUCK_TYPE_ID'][str(i)];
            shovelId[i] = data['SHOVEL_ID'][str(i)];
            dumpId[i] = data['DUMP_ID'][str(i)];

    with open('data.csv', 'w', newline='') as csvfile:
  # Create a CSV writer
        writer = csv.writer(csvfile)
  
  # Write a row with 11 columns
        for i in range(100002):
            writer.writerow([timestamp[i], north[i], east[i], elev[i], fuelRate[i], status[i], payload[i], truckId[i], typeId[i], shovelId[i], dumpId[i]])

            # print(data['TIMESTAMP'][str(i)], end=" | ")
            # print(data['GPSNORTHING'][str(i)], end=" | ")
            # print(data['GPSEASTING'][str(i)], end=" | ")
            # print(data['GPSELEVATION'][str(i)], end=" | ")
            # print(data['FUEL_RATE'][str(i)], end=" | ")
            # print(data['STATUS'][str(i)], end=" | ")
            # print(data['PAYLOAD'][str(i)], end=" | ")
            # print(data['TRUCK_ID'][str(i)], end=" | ")
            # print(data['TRUCK_TYPE_ID'][str(i)], end=" | ")
            # print(data['SHOVEL_ID'][str(i)], end=" | ")
            # print(data['DUMP_ID'][str(i)])