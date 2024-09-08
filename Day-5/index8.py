#WAP Print the elements of the following list using a loop: [1, 4, 9, 16, 25, 36, 49, 64, 81,100] 

# list = [1, 4, 9, 16, 25, 36, 49, 64, 81,100] 

# for i in list:
#     print(i)


#WAP Search for a number x in this tuple using loop: (1, 4, 9, 16, 25, 36, 49, 64, 81,100)

Tupal = (1, 4, 9, 16, 25, 36, 49, 64, 81,100)

num = 36

idx = 0

for el in Tupal:
    if(el == num):
        print("number found at idx " ,idx)
        # break
    idx +=1