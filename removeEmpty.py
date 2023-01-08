import csv

for t in range(69):
    for p in range(250):
        # fuelConsumed = 0
        # fuelPerMin = [0 for a in range(30)]
        try:
            with open(f'tripdata\\truck{t}_trip{p}.csv', 'r') as input_file:#, open(f"shovel{i}.csv", 'w', newline='') as output_file:
                # Filter out empty lines
                reader = csv.reader(input_file)
                non_empty_rows = filter(lambda row: any(row), reader)

                # Open the output CSV file
                with open(f'tripdata\\truck{t}_trip{p}.csv', "w", newline='') as f_out:
                    # Create a CSV writer object
                    writer = csv.writer(f_out)

                    # Write the non-empty rows to the output file
                    writer.writerows(non_empty_rows)
        except:
            blah = 0

    print(t)

        
            
    

          
          
