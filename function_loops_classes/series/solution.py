# Function to explicitly compute the geometric series sum
def geometric_series_explicit(x, N):
    sum_result = 0
    for k in range(N):
        sum_result += x ** k
    return sum_result

# Function to compute the geometric series using the closed-form formula
def geometric_series_closed(x, N):
    if x == 1:
        return N  # Special case where sum becomes simply N
    return (1 - x ** N) / (1 - x)

# Predefined x values
x_values = [0.1, 0.5, 0.9, 0.99]

# Maximum value of N
max_N = 50

# Dictionary to store test results where deviation is found
deviations = {}

# Tolerance for floating-point comparison
tolerance = 1e-10

# Compare explicit and closed-form results
for x in x_values:
    deviations[x] = []
    for N in range(1, max_N + 1):
        explicit = geometric_series_explicit(x, N)
        closed = geometric_series_closed(x, N)
        if abs(explicit - closed) > tolerance:
            deviations[x].append((N, explicit, closed))

# Displaying results
for x in deviations:
    if deviations[x]:
        print(f"\nFor x = {x}, differences found:")
        for d in deviations[x]:
            print(f"  N = {d[0]}: Explicit = {d[1]}, Closed-form = {d[2]}")
    else:
        print(f"\nFor x = {x}, both methods matched within tolerance.")