from collections import namedtuple, Counter

# NamedTuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(3, 4)
print("Point:", p)

# Counter
data = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
fruit_counter = Counter(data)
print("Fruit Count:", fruit_counter)
