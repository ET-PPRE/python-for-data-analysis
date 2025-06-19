#### 🎯 Task

In this excercise solar irradiance data from a `.txt` file should be read and used to perform basic calculations.

##### Part A

Extract data from the file **solar\_irradiance.txt**, which you can find in this directory, into a NumPy array called `irradiance_data`. The array should only contain irradiance data, not the timestamps.

**Note:** For this exercise, remove the 'Hour' column and the header from the data.

##### Part B 

Calculate the **average solar irradiance per day** in W/m² from the array `average_irradiance`. Save the result in a NumPy array named `average_irradiance` and print the result.

##### Part C

Calculate the Daily Energy Output of a solar power plant in MWh, using the following equation:

$$
\text{Energy Output (MWh)} = \frac{G \times A \times \eta}{10^6} \times t \times n
$$

Where:

- $A  = 1.8 \text{m}^2$ (area of one PV module) 

- $\eta = 0.2$ (efficiency)

- $n = 10.000$ (number of PV modules)

- $t = 24$ hours/day

- $G$ is the average irradiance in W/m² (taken from the irradiance data)

Save the results in an array called `daily_energy_output_pv`, and print the result.

#### 🔒 Restrictions

* **Use only numpy** 
* Follow the exact naming (`irradiance_data`, `average_irradiance`, `daily_energy_output_pv`).