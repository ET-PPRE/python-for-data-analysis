import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Data
x = [2001, 2003, 2005, 2007, 2009, 2011, 2013, 2015, 2017, 2019]
y = [15, 25, 35, 45, 50, 65, 70, 75, 80, 90]

# Create figure and axes
fig, ax = plt.subplots(figsize=(8, 6))

# Plot the data
ax.plot(x, y, color='red', linestyle='--')

# Customize labels and limits
ax.set_xlabel("Years")
ax.set_ylabel("Sales")
ax.set_xlim(2000, 2020)
ax.set_ylim(0, 100)

# Save the plot as a PNG file
fig.savefig("sales_plot.png", dpi=300)

# Show the plot
plt.show()