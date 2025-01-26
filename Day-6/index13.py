class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

student1 = Student("Bob", 22, "A")
print(f"Name: {student1.name}, Age: {student1.age}, Grade: {student1.grade}")
