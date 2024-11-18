# Define an array
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use filter() to get even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print("Even Numbers:", even_numbers)
