"""class Car:
    def __init__(self, model, brand):
        self.model = model
        self.brand = brand

    def setColor(self, color):
        self.color = color

    def getInfo(self):
        return self.__dict__

brichka = Car("x3", "bmw")
brichka.setColor("black")
print(brichka.getInfo())"""

class Car:
    def __init__(self, model, brand, color):
        self.model = model
        self.brand = brand
        self.color = color

brichka = Car("x3", "bmw", "black")
brichka.weight = 100
print(brichka.__dict__)
