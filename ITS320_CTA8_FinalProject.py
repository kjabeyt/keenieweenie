class Car:
    def __init__(self, make, model, color, year, mileage):
        self.make = make
        self.model = model
        self.color = color
        self.year = year
        self.mileage = mileage

    def add_vehicle(self):
        self.make = append(self.make)
        self.model = append(self.model)
        self.color = append(self.color)
        self.year = append(self.year)
        self.mileage = append(self.year)

    def remove_vehicle(self):
        self.make = remove(self.make)
        self.model = remove(self.model)
        self.color = remove(self.color)
        self.year = remove(self.year)
        self.mileage = remove(self.mileage)

    def update_vehicle_attributes(self):
        if self.make != self.make:
            self.make = self.make
        elif self.model != self.model:
            self.model = self.model
        elif self.color != self.color:
            self.color = self.color
        elif self.year != self.year:
            self.year = self.year
        elif self.mileage != self.mileage:
            self.mileage = self.mileage
car = {}


make = input('Enter make of car ex. Ford: ')
model = input('Enter model of make ex. Mustang: ')
color = input('Enter color of car: ')
year = int(input('Enter year of car: '))
mileage = int(input('Enter mileage: '))


