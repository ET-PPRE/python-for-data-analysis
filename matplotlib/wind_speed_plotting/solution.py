import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
data = pd.read_csv('measurements_2009.csv')

# Extract the WS-100 column to ws100
ws100 = data['WS-100']

# Create the plot
fig, ax = plt.subplots()
ax.plot(ws100)
ax.set_xlabel('Time')
ax.set_ylabel('Wind Speed at 100m [m/s]')
ax.set_title('Wind Speed Time Series')
plt.show()