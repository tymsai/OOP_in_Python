#elevate calss
class Elevator:
    occupied=8
    def __init__(self, occupants=0, floor=0):
        self.floor = floor
        if occupants<=Elevator.occupied:
            self.occupants<=occupants
        else:
            self.occupants=Elevator.occupied
            print('Too many occupants', occupants-Elevator.occupiec,' Left outside')
    def add_occupants(self, num):
        self.occupants+=num
        if self.occupants>Elevator.occupants:
            print('Too many occupants', self.occupants-Elevator.occupiec,' Left outside')
            self.occupants=Elevator.occupied
        
        pass
    def goto_floor(self, floor):
        if floor<-5 or floor >50:
            print('floor', floor, 'doesnt exist')
        else:
            self.floor=floor
        pass
elevator1=Elevator(6)
elevator1.add_occupants(7)
elevator2=Elevator(11)
elevator1.goto_floor(20)
print(elevator1.__dict__)
print(elevator2.__dict__)
