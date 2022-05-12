class Cat:
    def __init__(self, mass, lifespan, speed):
        self.mass_in_kg=mass
        self.lifespam_in_years=lifespan
        self.speed_in_kph=speed
    def sound(self):
        print('Meeeoww')
class Leopard(Cat):
    def __init__(self, mass, lifespan, speed, spotted=True):
        super().__init__(mass, lifespan, speed)
        self.spotted=spotted
    def sound(self):
        print('wwgghhrr')

tommy=Cat(50, 46, 56)
tommy.sound()
leo=Leopard(90, 13, 27, False)
leo.sound()
print(leo.__dict__)
print(tommy.__dict__)
