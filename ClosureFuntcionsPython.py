def Car(func):
    def Has_the_property(*_property):
        print(func(*_property))
    return Has_the_property

def Some_property(*_property):
    return f"{_property}"

addProperty = Car(Some_property)
addProperty(str(input()))

"""class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def _Property(self, isProperty):
        self.isProperty = isProperty


brichka = Car("Toyota", "Mark")
brichka._Property(str(input()))
print(brichka.__dict__)"""
