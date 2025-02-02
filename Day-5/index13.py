class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

class Car:
    def __init__(self, make, model, engine):
        self.make = make
        self.model = model
        self.engine = engine

engine = Engine(150)
car = Car("Toyota", "Corolla", engine)
print(f"Car: {car.make} {car.model}, Horsepower: {car.engine.horsepower}")