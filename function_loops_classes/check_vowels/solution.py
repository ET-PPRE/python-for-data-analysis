def contains_only_vowels(s):
    vowels = 'aeiou'
    for char in s:
        if char.lower() not in vowels:
            return "Not Only Vowels"
    return "Only Vowels"

# Predefined test strings
test_strings = ["eiou", "hello", "AaEeIiOoUu"]

# Test the function on predefined test strings
for test_string in test_strings:
    result = contains_only_vowels(test_string)
    print(f"Input: '{test_string}' -> Output: {result}")
