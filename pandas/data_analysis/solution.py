import pandas as pd

# Create the DataFrame with the specified data
df = pd.DataFrame({
    'Employee_ID': [1, 2, 3, 4, 5],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [28, 34, 45, 31, 29],
    'Performance_Score': [85, 72, 90, 60, 78]
})

# Filter for employees older than 30 and Performance Score >= 70
eligible_for_promotion = df[
    (df['Age'] > 30) &
    (df['Performance_Score'] >= 70)
]

print(eligible_for_promotion)