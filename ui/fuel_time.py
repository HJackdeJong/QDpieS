import matplotlib.pyplot as plt
import csv
data = []
with open('trip0.csv') as csvfile:
    reader = csv.reader(csvfile)
    # Skip every other 299 rows
    for i,  row in enumerate(reader):
        try:
            if row[4] == '':
                fuel = 0
            else :
                fuel = row[4]
            data.append( (int(row[0]), float(fuel) ))
        except:
            print(row)

# Time data (assuming data points are collected at a rate of one per second)
times, fuel_usage = zip(*data)

# Plot the data

plt.plot(times, fuel_usage)

# Add axis labels and a title
plt.xlabel('Time')
plt.ylabel('Fuel usage (l)')
plt.title('Fuel Usage vs Time')
plt.ylim(0, 250)

# Show the plot
plt.show()
