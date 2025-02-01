class Employee:
    employee_count = 0

    def __init__(self, name):
        self.name = name
        Employee.employee_count += 1

    @classmethod
    def total_employees(cls):
        return cls.employee_count

emp1 = Employee("Alice")
emp2 = Employee("Bob")
print("Total employees:", Employee.total_employees())
