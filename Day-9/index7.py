class Pareson:
    name = "anonymous"

    # def changeName(self, name):
    #     # self.name = name          anonymous
    #     Pareson.name = name
    #     self.__class__.name = "Rahul"

    @classmethod
    def changeName(cls,name):
        cls.name = name

p1 = Pareson()
p1.changeName("Rahul kumar")
print(p1.name)
print(Pareson.name)