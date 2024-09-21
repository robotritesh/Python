#Create student class that takes name & marks of 3 subjects as arguments in constructor. 
# Then create a method to print the average.

class Student:
    def __init__ (self, name, marks):
        self.name = name
        self.marks = marks


    def get_avg(self):
        sum = 0 
        for val in self.marks:
            sum += val
        print("Hi", self.name, "your avg score is", sum/3)

s1 = Student("tony stark", [99, 98, 97])
s1.get_avg()

s1.name = "ironman"
s1.get_avg()