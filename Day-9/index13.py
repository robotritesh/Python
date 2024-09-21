class Employee:
    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary

    def showNumber(self):
        print("role =", self.role)
        print("dept =", self.dept)
        print("salary =", self.salary)

class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("Engineer", "IT", "75,000")

engg1 = Engineer("SDE", 21)
engg1.showNumber()

# e1 = Employee("accountant", "finace", "60,000")
# e1.showNumber()