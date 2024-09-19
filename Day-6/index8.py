# def number(num):
#     if (num == 0):
#         return 0
#     return number(num-1) + num

# sum = number(5)

# print(sum)  //5 4 3 2 1

def number(num):
    if (num == 0):
        return
    number(num-1)
    print(num)


number(5)
