#WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with an empty dictionary & add one by one. Use subject name as key & marks as value. 
dict1 = {}

# dict1["mathematics"] = 51

# dict1["physics"] = 78

# dict1["chemistry"] = 78

# ||       or          ||

x = int(input(" enter mathematics :"))
dict1.update({"mathematics":x})

x = int(input(" enter physics :"))
dict1.update({"physics":x})

x = int(input(" enter chemistry :"))
dict1.update({"chemistry":x})

print(dict1)