def show(n):
    if(n == 0):
        return
    print(n)
    show(n-1)  #reverce

show(5)