# Load data into a list of lists

for j in range(69):
  data = []
  with open(f'trucks\\truck{j}.csv', 'r') as f:
    for line in f:
      data.append(line.strip().split(','))

  # Iterate through rows of data
  for i in range(1, len(data)-1):
    # Check if current status is different from previous and next status
    if data[i][5] != data[i-1][5] and data[i][5] != data[i+1][5]:
      # Change current status to previous status
      data[i][5] = data[i-1][5]

  # Save cleaned data to a new file
  with open(f'cleaned_trucks\\cleaned_truck{j}.csv', 'w') as f:
    for row in data:
      f.write(','.join(row) + '\n')
