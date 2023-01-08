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
    with open(f'fuel\\truck{t}_fuel.csv', 'w') as file:
        print(f"trip,"+ "median," +"mean",file=file)
        for p in range(250):
            try:
                fuelConsumedMedian = 0
                fuelConsumedMean = 0
                fuelPerMin = [0 for a in range(30)]
                with open(f'tripdata\\truck{t}_trip{p}.csv', 'r') as input_file:#, open(f"shovel{i}.csv", 'w', newline='') as output_file:
                    # Create a CSV reader and writer
                    reader = csv.reader(input_file)
                    for row in reader:
                        try:
                            # i+=1
                            # print(i)
                            if count < 30:
                                fuelPerMin[count] = float(row[4])
                                count += 1
                            else:
                                fuelConsumedMedian += (statistics.median(fuelPerMin)*(1/60))
                                fuelConsumedMean += (statistics.mean(fuelPerMin)*(1/60))


                                fuelPerMin = [0 for a in range(30)]
                                count = 0
                        except:
                            i = 0

                print(f"{p},"+ str(round(fuelConsumedMedian, 2)) +"," +str(round(fuelConsumedMean, 2)),file=file)
                totalMedian += fuelConsumedMedian
                totalMean += fuelConsumedMean
            except:
                p = 250
        print(f"-1,"+ str(totalMedian) +"," +str(totalMean),file=file)
        

            
            
