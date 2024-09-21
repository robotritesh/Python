class Student:
    def __init__(self,marks):
        self.marks = marks

    def welcome(self):
        print("Welcome Student")

    def get_marks(self):
        return self.marks
        

s1 = Student(95)
s1.welcome()
print(s1.get_marks())