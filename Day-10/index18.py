# Input: A list of numbers
numbers = [34, 7, 23, 32, 5, 62]

# Sort in ascending order
ascending_sorted = sorted(numbers)
print("Ascending Order:", ascending_sorted)

# Sort in descending order
descending_sorted = sorted(numbers, reverse=True)
print("Descending Order:", descending_sorted)

# Custom sorting (example: sort by the remainder when divided by 3)
custom_sorted = sorted(numbers, key=lambda x: x % 3)
print("Custom Order (by remainder when divided by 3):", custom_sorted)

# Using list's sort method (modifies the original list)
numbers.sort()
print("In-place Sorted List (Ascending):", numbers)
