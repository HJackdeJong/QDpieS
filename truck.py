import csv

# Open the input and output files
max = 32
for i in range(max):
    with open('data2.csv', 'r') as input_file, open(f"truck{i}.csv", 'w', newline='') as output_file:
        # Create a CSV reader and writer
        reader = csv.reader(input_file)
        writer = csv.writer(output_file)

        # # Iterate over the rows in the input file
        for row in reader:
            # Check if the 8th column is 0
            if int(row[7]) == i:
                max = int(row[7])
                writer.writerow(row)
