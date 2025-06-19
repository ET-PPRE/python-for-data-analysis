import numpy as np

def array_operations():
    # Create a NumPy array from 1 to 10
    arr = np.arange(1, 11)
    
    # Calculate the sum and mean
    total_sum = np.sum(arr)
    mean_value = np.mean(arr)
    
    # Print the results
    print(f'Original Array: {arr}')
    print(f'Sum of Array: {total_sum}')
    print(f'Mean of Array: {mean_value}')
    
    return total_sum, mean_value

# Call the function
arr_sum, arr_mean = array_operations()