# Using `with` for automatic file management
with open("sample.txt", "w") as file:
    file.write("Hello, Python!")

# File will be automatically closed outside of `with` block
