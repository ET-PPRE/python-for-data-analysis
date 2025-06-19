import pandas as pd

# Import the dataset into a DataFrame
power_data = pd.read_csv('power_generation_data.csv')

# Inspect the first 5 rows
data_inspection = power_data.head(5)

# Check for missing values and save the sum
missing_values = power_data.isnull().sum()

# Fill missing values using forward fill and save as new DataFrame
clean_data = power_data.fillna(method='ffill')

print(clean_data.head())