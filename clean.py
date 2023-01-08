import csv
for j in range(69):
    print(j)
    # Read in the data from the file
    with open(f'cleaned_trucks\\cleaned_truck{j}.csv', 'r') as f:
        reader = csv.DictReader(f)
        data = list(reader)

    # Initialize a dictionary with the column names as keys and empty lists as values
    cleaned_data = {col: [] for col in reader.fieldnames}

    # Iterate through each row of the data
    for row in data:
        # For each column that is null, set the value to the last non-null value in that column
        for col in cleaned_data:
            if not row[col]:
                try:
                    row[col] = cleaned_data[col][-1]
                except:
                    row[col] = '0.0'
        # Append the cleaned values to the corresponding lists in the dictionary
        for col in cleaned_data:
            cleaned_data[col].append(row[col])

    # Create a new list of dictionaries, with each dictionary representing a row of cleaned data
    cleaned_data_list = [{col: value for col, value in zip(cleaned_data, row_values)} for row_values in zip(*cleaned_data.values())]

    # Write the cleaned data to a new file
    with open(f'cleaned_trucks\\cleaned_truck{j}.csv', 'w') as f:
        writer = csv.DictWriter(f, fieldnames=reader.fieldnames, lineterminator='\n')
        writer.writeheader()
        writer.writerows(cleaned_data_list)