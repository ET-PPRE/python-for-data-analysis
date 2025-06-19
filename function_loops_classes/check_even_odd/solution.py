def check_even_odd(number):
    # Check if the number is even or odd
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Predefined list of numbers
numbers_to_test = [10, 7, 22, 15, 0]

# Loop through the list and check each number
for number in numbers_to_test:
    result = check_even_odd(number)
    print(f"Number: {number} is {result}")
