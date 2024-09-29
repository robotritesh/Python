# last_num = []

# for i in range(1,51):
#     if(i%5 == 0):
#         last_num = [:-5]
#     print(last_num)

last_num = []

for i in range(1, 51):
    if i % 5 == 0:
        last_num.append(i)

print(last_num[-5:])