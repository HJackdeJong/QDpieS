import csv
import statistics

for t in range(69):
    # Open the input and output files
    print(t)
    fuelConsumedMedian = 0
    fuelConsumedMean = 0
    totalMedian = 0
    totalMean = 0
    count = 0
    i = 0
    fuelPerMin = [0 for a in range(30)]
    with open(f'/home/justin/Desktop/BCIT Share/repos/QDpieS/truck_fuel/truck{t}_fuel.csv', 'w') as file:
        print(f"trip,"+ "median," +"mean,numRowsIdle,numRowsNotIdle",file=file)
        for p in range(250):
            try:
                fuelConsumedMedian = 0
                fuelConsumedMean = 0
                numRowsIdle = 0
                numRowsNotIdle = 0
                fuelPerIdle = []
                with open(f'/home/justin/Desktop/BCIT Share/repos/QDpieS/tripdata/truck{t}_trip{p}.csv', 'r') as input_file:#, open(f"shovel{i}.csv", 'w', newline='') as output_file:
                    # Create a CSV reader and writer
                    reader = csv.reader(input_file)
                    for row in reader:
                        try:
                            # i+=1
                            # print(i)
                            if "Queue" in row[5]:
                                fuelPerIdle.append(float(row[4]))
                                # print(float(row[4]))
                                # print(row[5])
                                # print()
                                numRowsIdle += 1
                            else:
                                numRowsNotIdle += 1
                        except:
                            i = 0
                fuelConsumedMedian += (statistics.median(fuelPerIdle)*(1/numRowsIdle * 2))
                fuelConsumedMean += (statistics.mean(fuelPerIdle)*(1/numRowsIdle * 2))
                print(f"{p},"+ str(round(fuelConsumedMedian, 2)) +"," +str(round(fuelConsumedMean, 2))+","+str(numRowsIdle)+","+str(numRowsNotIdle),file=file)
                totalMedian += fuelConsumedMedian
                totalMean += fuelConsumedMean
            except:
                p = 250
        print(f"-1,"+ str(totalMedian) +"," +str(totalMean),file=file)
        
