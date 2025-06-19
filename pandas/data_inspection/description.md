#### 🎯 Task

The goal of this exercise is to work with a simulated dataset containing solar and wind power generation data, and to perform the primary inspection before cleaning and processing, visualizing and analyzing it.

Import the dataset **power_generation_data.csv** into a Pandas DataFrame called `power_data`. This file is avaialble to you in this directory, there is no need to state the file path while you import, **only the file name**. Check the first 5 rows of the dataset to get an overview of the data, save these rows into a variable called `data_inspection`.

Perform basic inspection to understand the data types and structure. Check for missing values in the dataset, save the sum of the missing values into a variable called `missing_values`.

It is common that there is missing values within the dataset, therefore handling missing value is a typical task of data processing. Handle the missing values you detected by filling them using forward filling. Save the dataframe with the filled missing values into a new DataFrame called `clean_data`.

#### 🔒 Restrictions

* **Use only pandas** 
* Follow the exact naming (`power_data`, `data_inspection`, `missing_values`, `clean_data`).