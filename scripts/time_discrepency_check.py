"""
    prints the time deltas to make scanning for time discrepencies easier
"""

import csv
import datetime  

with open("/home/justin/Desktop/BCIT Share/repos/QDpieS/truck_data/truck0.csv") as file:
    csvreader = csv.reader(file)

    prevEpoch = 0
    for i, row in enumerate(csvreader):
        curEpoch = int(row[0]) # timestamp
        # print(curEpoch) 
        date = datetime.datetime.fromtimestamp( curEpoch / 1000 ) # converts epoch to date stamp
        print(date.strftime("day%d:second%S"), (curEpoch - prevEpoch) / 1000,"s", ": ", row)
        prevEpoch = curEpoch
