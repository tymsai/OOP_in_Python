#%%
class Car:
    def __init__(self, make, model, year):
        self.make=make
        self.model=model
        self.year=year
    def get_make(self):
        return self._make
    def get_model(self):
        return self._model
    def get_year(self):
        return self._year
    def set_model(self, new_model):
        self._model=new_model
        
mycar= Car('mazda', 15, 2016)
print(mycar.model)
mycar.set_model('6x')
print(mycar.get_make)
print(mycar.__dict__)
