import csv

# Open the input and output files
max = 69
s = ""
for i in range(max):
    count = [0,0,0,0,0,0,0,0,0]
    with open(f'truck{i}.csv', 'r') as input_file, open(f"truckStatus{i}.csv", 'w', newline='') as output_file:
        # Create a CSV reader and writer
        reader = csv.reader(input_file)
        writer = csv.writer(output_file)

        # # Iterate over the rows in the input file
        for row in reader:
            # Check if the 8th column is 0
            status = row[5]
            if status == "Empty":
                count[0] += 1
            elif status == "Queue At LU":
                count[1] += 1
            elif status == "Spot at LU":
                count[2] += 1
            elif status == "Truck Loading":
                count[3] += 1
            elif status == "Hauling":
                count[4] += 1
            elif status == "Queuing at Dump":
                count[5] += 1
            elif status == "Dumping":
                count[6] += 1
            elif status == "NON_PRODUCTIVE":
                count[7] += 1
            elif status == "Wenco General Production":
                count[8] += 1
    print(f"Empty {count[0]}\nQueue At LU {count[1]}\nSpot at LU {count[2]}\nTruck Loading {count[3]}\nHauling {count[4]}\nQueuing at Dump {count[5]}\nDumping {count[6]}\nNON_PRODUCTIVE {count[7]}\nWenco General Production {count[8]}")