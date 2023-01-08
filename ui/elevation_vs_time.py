import matplotlib.pyplot as plt
import datetime
from matplotlib.dates import DateFormatter
import csv

# Elevation data
# data = [
#     (1.64931E+12, 335.8432),
#     (1.64931E+12, 335.9244),
#     (1.64931E+12, 335.9244),
#     (1.64931E+12, 335.6402),
#     (1.64931E+12, 335.0718),
# ]
data = []
print("reading data")
with open('trip0.csv') as csvfile:
    reader = csv.reader(csvfile)
    # Skip every other 299 rows
    for i,  row in enumerate(reader):
        try:
            if row[0] == '' or row[3] == '':
                continue
            data.append( (int(row[0]), float( row[3] )) )
        except:
            print(row)

print("reading done")
print("plotting")
 # Extract time and elevation data
times, elevations = zip(*data)

# Convert times to human-readable format
times = [datetime.datetime.fromtimestamp(t/1000) for t in times]

# Plot the data
plt.plot(times, elevations)

# Add axis labels and a title
plt.xlabel('Time')
plt.ylabel('Elevation (m)')
plt.title('Elevation vs Time')

# Set the x-axis tick labels to only show the time of day
formatter = DateFormatter('%H:%M:%S')
plt.gca().xaxis.set_major_formatter(formatter)

# Show the plot
plt.show()

print("plotting done")