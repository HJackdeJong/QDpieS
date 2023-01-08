"""
    This script will calculate the min/max
    values of northing, easting, and elevation
    to help us scale our route visualizations
"""

import csv

for i in range(69):
    with open(f"/home/justin/Desktop/BCIT Share/repos/QDpieS/truck_data/truck{i}.csv") as file:
        csvreader = csv.reader(file)


        prevStatus = ""
        count = 0
        for row in csvreader:
            curStatus = row[5]

            if curStatus not in headers.keys():
                headers[curStatus] = 0
            else:
                headers[curStatus] += 1

            if curStatus == prevStatus:
                count += 1

            else:
                prevStatus = curStatus
                if count != 0:
                    print(curStatus.ljust(16, " "), ":", count * 2, "seconds")
                count = 0


print(headers)