class Vehicle:
    def start(self):
        print("Starting the vehicle...")

class Car(Vehicle):
    def start(self):
        print("Starting the car...")

vehicle = Vehicle()
vehicle.start()

car = Car()
car.start()
