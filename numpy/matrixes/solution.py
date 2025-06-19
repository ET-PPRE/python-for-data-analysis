import numpy as np

def matrix_operations():
    # Create Matrix A (3x2)
    A = np.array([[1, 2],
                  [3, 4],
                  [5, 6]])
    
    # Create Matrix B (2x3)
    B = np.array([[7, 8, 9],
                  [10, 11, 12]])
    
    # Multiply Matrix A by Matrix B to get Matrix C
    C = np.dot(A, B)
    
    # Transpose Matrix C to get Matrix D
    D = C.T
    
    # Print the results
    print("Matrix A:")
    print(A)
    print("\nMatrix B:")
    print(B)
    print("\nMatrix C (A * B):")
    print(C)
    print("\nMatrix D (Transpose of C):")
    print(D)
    return A, B, C, D

# Call the function
A, B, C, D = matrix_operations()