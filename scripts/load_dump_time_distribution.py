"""
    calculate the distribution of times (10 second 'buckets')
    it takes to load, and dump.
"""

import csv
import math

load_distribution = {}
for i in range(0, 1500, 10):
    load_distribution[i] = 0


dump_distribution = {}
for i in range(0, 1500, 10):
    dump_distribution[i] = 0

def roundup(x):
    return int(math.ceil(x / 10.0)) * 10


for i in range(69):
    with open(f"/home/justin/Desktop/BCIT Share/repos/QDpieS/truck_data/truck{i}.csv") as file:
        csvreader = csv.reader(file)

        prevStatus = ""
        count = 0
        for row in csvreader:
            curStatus = row[5]

            # if curStatus not in headers.keys():
            #     headers[curStatus] = 0
            # else:
            #     headers[curStatus] += 1

            if curStatus == prevStatus:
                count += 1

            else:
                prevStatus = curStatus
                if count != 0:
                    if(curStatus == "Dumping"):
                        try:
                            dump_distribution[roundup(count * 2)] += 1
                        except:
                            pass
                        # print("dump: ", curStatus.ljust(16, " "), ":", roundup(count * 2) , "seconds")
                        
                    if(curStatus == "Truck Loading"):
                        try:
                            load_distribution[roundup(count * 2)] += 1
                        except:
                            pass
                        # print("truck loading: ", curStatus.ljust(16, " "), ":", roundup(count * 2) , "seconds")

                    count = 0
                    
                

print(load_distribution)
print("\n\n\n\n\n\n\n")
print(dump_distribution)

sum = 0
for i in range(0, 600, 10):
    sum += dump_distribution[i]
    sum += load_distribution[i]

    # if sum > 8512:3
        # print(key)
        # break

print(sum)

