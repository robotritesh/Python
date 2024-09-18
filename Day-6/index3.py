# //n = 5 //5!

# // for i in Range(1, n+1):
# //     fact *= i

# // print(fact)

def cal_fact(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    print(fact)

cal_fact(6)

