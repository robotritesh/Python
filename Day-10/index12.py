# Unpacking lists with *
nums = [1, 2, 3]
print("Numbers:", *nums)  # Outputs: 1 2 3

# Unpacking dictionary with **
person = {"name": "Alice", "age": 25}
def greet(name, age):
    print(f"Hello, {name}! You are {age} years old.")

greet(**person)
