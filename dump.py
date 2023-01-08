import csv

# Open the input and output files
shovelMax = 8
dumpMax = 30
north = 0
east = 0
count = 0
shovel = 0
shovelsCount = [0 for a in range(31)]
shovelsNorth = [0 for a in range(31)]
shovelsEast = [0 for a in range(31)]
shovelsElev = [0 for a in range(31)]
with open(f'cleaned_data2.csv', 'r') as input_file:#, open(f"shovel{i}.csv", 'w', newline='') as output_file:
    # Create a CSV reader and writer
    reader = csv.reader(input_file)
    for row in reader:
        if row[5] == "Dumping":
            shovel = int(row[10])
            if row[1] != "" and row[2] !="" and row[3] !="":
                shovelsNorth[shovel] += float(row[1])
                shovelsEast[shovel] += float(row[2])
                shovelsElev[shovel] += float(row[3])
                shovelsCount[shovel] += 1
    print("________________________________________")
    print("________________________________________")
    print("________________________________________")
    for i in range(31):
        try:
            print("dump: " + str(i) + " | north: " + str(shovelsNorth[i]/shovelsCount[i]) + " | east: " + str(shovelsEast[i]/shovelsCount[i]) + " | elev: " + str(shovelsElev[i]/shovelsCount[i]))
        except:
            count = 0
