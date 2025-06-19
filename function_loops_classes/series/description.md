#### 🎯 Task

1. Write a function that explicitly calculates the sum of the series:

    $$ \sum_{i=0}^{n-1} x^i = x^0 + x^1 + x^2 + \dots + x^{n-1} $$

    where N is a positive integer and x is a number.
    (You must add each term one by one.)

2. Write another function that calculates the closed-form formula:

    $$ \sum_{i=0}^{N-1} x^i = \frac{1 - x^N}{1 - x} $$

3. Compare the two functions:

    For 0 < x < 1, check if both functions give the same result.

    Test for all N from 1 to 50, and pick four different values for x, such as `[0.1, 0.5, 0.9, 0.99]`.

#### 🔒 Restrictions

* **Do not use any external libraries** (e.g., no `numpy`, `math`, etc.).
* Follow the exact naming (`geometric_series_explicit`, `geometric_series_closed`).
* The x-values must be stored exactly as: x_values = [0.1, 0.5, 0.9, 0.99]