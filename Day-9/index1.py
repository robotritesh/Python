class acount:
    def __init__(self,acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass      #__ it is privet

    def reset_pass(self):
        print(self.__acc_pass)

acc1 = acount("12345","abcde")

print(acc1.acc_no)
#print(acc1.__acc_pass)                 #__ it is privet
print(acc1.reset_pass())   