import array

# Creating an array
numbers = array.array('i', [10, 20, 30, 40, 50])  # 'i' denotes an array of integers

# Displaying the array
print("Array elements:", numbers)

# Accessing elements
print("First element:", numbers[0])
print("Last element:", numbers[-1])

# Adding elements
numbers.append(60)
print("After appending 60:", numbers)

# Inserting an element at a specific position
numbers.insert(2, 25)
print("After inserting 25 at index 2:", numbers)

# Removing an element
numbers.remove(30)
print("After removing 30:", numbers)

# Popping an element
popped_element = numbers.pop()
print("After popping an element:", numbers)
print("Popped element:", popped_element)

# Updating an element
numbers[1] = 100
print("After updating the second element to 100:", numbers)

# Iterating through the array
print("Iterating through the array:")
for num in numbers:
    print(num, end=" ")
print()

# Length of the array
print("Length of the array:", len(numbers))
