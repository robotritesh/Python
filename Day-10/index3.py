# Create a list of numbers that are both even and greater than 10
numbers = [5, 12, 7, 18, 22, 3]
filtered_numbers = [x for x in numbers if x % 2 == 0 and x > 10]
print("Filtered Numbers:", filtered_numbers)
