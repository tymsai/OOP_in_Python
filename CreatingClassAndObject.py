
#Object oriented programming
class Car():
    pass
honda=Car()
mazda=Car()
honda.model='CRV'
honda.weight='1.5 Ton'
print('Honda Model', honda.model)
print('Honda Weight', honda.weight)
print(honda.__dict__)
