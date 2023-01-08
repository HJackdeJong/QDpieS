import pandas as pd

# Load the data into a Pandas DataFrame
df = pd.read_csv('testdata.csv')


# Fill missing values with 0
df.fillna(0, inplace=True)

# Convert the timestamp column to a datetime
df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')



# Remove negative values from the fuelRate column
df = df[df['fuelRate'] >= 0]

# Remove outliers from the fuelRate column
q1 = df['fuelRate'].quantile(0.25)
q3 = df['fuelRate'].quantile(0.75)
iqr = q3 - q1
lower_bound = q1 - (1.5 * iqr)
upper_bound = q3 + (1.5 * iqr)
df = df[(df['fuelRate'] > lower_bound) & (df['fuelRate'] < upper_bound)]

# Save the cleaned data to a new CSV file
df.to_csv('cleaned_data.csv', index=False)