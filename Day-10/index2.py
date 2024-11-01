from functools import reduce

# map function
nums = [1, 2, 3, 4]
squared = list(map(lambda x: x ** 2, nums))
print("Squared:", squared)

# filter function
evens = list(filter(lambda x: x % 2 == 0, nums))
print("Evens:", evens)

# reduce function
product = reduce(lambda x, y: x * y, nums)
print("Product of nums:", product)
