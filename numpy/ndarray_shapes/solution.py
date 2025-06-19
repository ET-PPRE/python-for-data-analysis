import numpy as np

def reshape_array():
    # Create a 1D NumPy array from 1 to 12
    arr = np.arange(1, 13)
    
    # Reshape it to a 2D array of shape (3, 4)
    reshaped_arr = arr.reshape(3, 4)
    
    # Print the results
    print(f'Original Array: {arr}')
    print('Reshaped Array:')
    print(reshaped_arr)
    
    return arr, reshaped_arr

# Call the function
reshape_array()