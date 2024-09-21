class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.cltuch = False

    def start(self):
        self.cltuch = True
        self.acc = True
        print("car is start..")

car1 = Car()
car1.start()