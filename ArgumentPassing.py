import math
class Weight():
    def area(self, r):
        return math.pi*r*r
obj=Weight()
r=int(input("Enter the radius of circle"))
print(obj.area(r))
