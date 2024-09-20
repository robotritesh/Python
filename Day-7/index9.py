# with open("Day-7/demo.tex","r") as f:
#     data = f.read()
#     print(data)

#     nums = data.split(",")
#     print(nums)
count = 0
with open("Day-7/demo.tex", "r") as f:
    data = f.read()
    
    nums = data.split(",") 
    for val in nums:
        if(int(val) % 2 == 0):
            count += 1

print(count)