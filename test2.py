class Car:
    def __init__(self, model, company):
        self.model = model
        self.company = company
    def PrintCar(self):
        print(self.model, self.company)

if __name__ == "__main__":
    newCar = Car("180sx", "nissan")
    newCar.PrintCar()
