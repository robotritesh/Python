sub = {
    "name" : "Ritesh",
    "age" : 21,
    "college" : "BIRT",     #dict
    "alph" : {
        "A":1,
        "B":2
    }
}

# print(len(list(sub.keys())))

# print(list(sub.keys()))

# print(list(sub.values()))



# print(sub.items())

# print(list(sub.items()))  #it is give the O/P in tupalin ()

# pairs = list(sub.items())

# print(pairs[0])


# print(sub["name"])
# print(sub.get("name"))

# print(sub["name1"])  #error
# print(sub.get("name1"))   #None

new_dict = {"city":"Bhopal"}
sub.update(new_dict)

print(sub)