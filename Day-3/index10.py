def func(x, y=[]):
    y.append(x)
    return y

print(func(1))
print(func(2))
print(func(3, []))
print(func(4))
