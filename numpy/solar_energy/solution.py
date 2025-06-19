import numpy as np

# Part A: Read data from the file and store the irradiance data in a NumPy array
irradiance_data = np.genfromtxt('solar_irradiance.txt', skip_header=1, usecols=range(1, 8))

# Print the irradiance data to check
print("Irradiance Data:")
print(irradiance_data)

# Part B: Calculate the average solar irradiance per day (average for each of the 7 columns)
average_irradiance = np.mean(irradiance_data, axis=0)

# Print the average solar irradiance per day for each of the 7 days of the week
print("Average Solar Irradiance per Day (W/m²):")
print(average_irradiance)


# Part C: Calculate the Daily Energy Output of the solar power plant in MWh

# Constants
area_of_module = 1.8  # m² (Area of one PV module)
efficiency = 0.2  # Efficiency of the solar panels
number_of_modules = 10000  # Number of PV modules
t = 24  # hours/day

# Calculate daily energy output in MWh for each day of the week using the formula
# Energy Output (MWh) = (G * A * η / 10^6) * t * n
daily_energy_output_pv = (average_irradiance * area_of_module * efficiency / 1e6) * number_of_modules * t

# Print the daily energy output in MWh for each of the 7 days
print("Daily Energy Output (MWh):")
print(daily_energy_output_pv)