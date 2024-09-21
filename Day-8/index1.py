class Student:
    def __init__(self,fullname,marks):
        self.name = fullname
        self.marks = marks
        print("it is Python")

s1 = Student("Ritesh",81)
print(s1.name,s1.marks)