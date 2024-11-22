# Function to check if a number is greater than 5
def is_greater_than_five(num):
    return num > 5

# Array of numbers
numbers = [1, 3, 5, 7, 9, 11]

# Filter using the function
greater_numbers = list(filter(is_greater_than_five, numbers))

print("Numbers greater than 5:", greater_numbers)
