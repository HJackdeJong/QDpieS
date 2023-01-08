import csv


for truck in range(66,69):
    trips = ["" for a in range(500000)]
    count = 0
    dumping = 0
    tripNum = 0
    # Open the input and output files
    with open(f'cleaned_trucks\\cleaned_truck{truck}.csv', 'r') as input_file:
        reader = csv.reader(input_file)
        j = 0
        for row in reader:
                if (row[5] == "Dumping" and dumping == 0):
                    dumping = 1
                if (row[5] == "Empty" and dumping == 1):
                    dumping = 0
                    with open(f'tripdata\\truck{truck}_trip{tripNum}.csv', 'w', newline='') as output_file:
                        trips = [x for x in trips if x != ""]
                        for trip in trips:
                                writer = csv.writer(output_file)
                                writer.writerow(trip)
                        trips = ["" for a in range(500000)]
                        count = 0
                    tripNum +=1
                trips[count] = row
                count +=1