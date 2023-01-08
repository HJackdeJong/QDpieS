import matplotlib.pyplot as plt
import pandas as pd
import datetime

data = pd.read_csv("truck1.csv")


timestamps = []
fuel_rates = []

# Convert timestamps to datetime objects
timestamps = [datetime.datetime.fromtimestamp(t/1000) for t in data.iloc[:,0]]
fuel_rates = data.iloc[:,4]

# Calculate the time delta between the first datapoint and the next hour
start_time = timestamps[0]
end_time = start_time + datetime.timedelta(hours=1)

filtered_timestamps = []
filtered_fuel_rates = []

for i in range(len(timestamps)):
    if timestamps[i] < end_time:
        filtered_timestamps.append(timestamps[i])
        filtered_fuel_rates.append(fuel_rates[i])

# Plot the data using matplotlib
plt.plot(filtered_timestamps, filtered_fuel_rates)

# Format the x-axis labels as dates
plt.gcf().autofmt_xdate()

plt.xlabel("Time")
plt.ylabel("Fuel Rate (litres/hour)")
plt.title("Fuel Rate Over Time")
plt.show()
