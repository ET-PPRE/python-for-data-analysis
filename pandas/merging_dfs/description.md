#### 🎯 Task

Merge two DataFrames on a common key and perform basic data analysis.

#### 1. Create the following DataFrames

- **DataFrame A**  
  - Columns: `['Employee_ID', 'Name']`  
  - Data:
    ```
    [[1, 'Alice'],
     [2, 'Bob'],
     [3, 'Charlie']]
    ```

- **DataFrame B**  
  - Columns: `['Employee_ID', 'Salary']`  
  - Data:
    ```
    [[1, 70000],
     [2, 80000],
     [4, 90000]]
    ```

#### 2. Merge the DataFrames

- Merge **DataFrame A** and **DataFrame B** on the `Employee_ID` column using an **inner join**.
- Store the result in a new DataFrame called `merged_df1`.

#### 3. Perform Analysis

- Calculate the `average_salary` from `merged_df1`.
- Display:
  - The merged DataFrame `merged_df1`
  - The `average_salary`

#### 🔒 Restrictions

* **Use only pandas** 
* Follow the exact naming (`A`, `B`, `['Employee_ID', 'Name', 'Salary']`, `merged_df1`, `average_salary` ).