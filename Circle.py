import math
class Circle2D:
    def __init__(self,r):
        self.__rad = r

    @property
    def rad(self):
        return self.__rad

    @rad.setter
    def rad(self,r):
        self.__rad = r

    def computeCircumference(self):
        return math.pi * self.__rad

    def computeArea(self):
        return math.pi * self.__rad**2

class Circle3D(Circle2D):
    def __init__(self,r,x):
       Circle2D.__init__ (self ,r)
       self.__color = x

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self,x):
        self.__color = x

    def sphereVolume(self):
        return 4/3 * math.pi * OBone.rad**3

print('start')
c = Circle2D(6)
print('1','=',c.rad)
c.rad = 5
print('2','=',c.rad)
print('3','=',c.computeArea())
print('4','=',c.computeCircumference())
OBone = Circle3D(2,'red')
print('5','=',OBone.color)
OBone.color = 'pink'
print('6','=',OBone.color)
print('7','=',OBone.spehereVolume())
