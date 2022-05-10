
#__init__Method (initilisation Method)
class Car():
    def __init__(self, make, model, year):
        self.make=make
        self.model=model
        self.year=year
mycar= Car('mazda', 2016, '1500kg')
yourcar=Car('honda', 2017, '1800kg')
print(mycar.__dict__)
print(yourcar.__dict__)
