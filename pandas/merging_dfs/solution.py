import pandas as pd
import numpy as np

data_a = [[1, 'Alice'], [2, 'Bob'], [3, 'Charlie']]
columns_a = ['Employee_ID', 'Name']
A = pd.DataFrame(data_a, columns=columns_a)

data_b = [[1, 70000], [2, 80000], [4, 90000]]
columns_b = ['Employee_ID', 'Salary']
B = pd.DataFrame(data_b, columns=columns_b)

merged_df1 = pd.merge(A, B, on='Employee_ID', how='inner')

average_salary = merged_df1['Salary'].mean()

print("DataFrame A:")
print(A)
print("\n DataFrame B:")
print(B)
print("\n Merged DataFrame (Inner Join on Employee_ID):")
print(merged_df1)
print(f"\n Average Salary from merged_df1: ${average_salary:.2f}")