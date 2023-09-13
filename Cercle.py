import math
class Point:
    def __init__(self,__x=0,__y=None):
        if __y is None:
            __y = __x
        self.__x = __x
        self.__y = __y
    def getX(self):
        return self.__x
    def setX(self,x):
        self.__x=x
    def getY(self):
        return self.__y
    def setY(self,y):
        self.__y=y
    def afficher(self):
        return f"({self.__x},{self.__y})"
    def deplacer(self,dx,dy):
        self.__x+=dx
        self.__y+=dy
    def distance(self,other):
        return math.sqrt((self.__x-other.__x)**2 + (self.__y-other.__y)**2)

    def millieu(self):
        return self.distance(other=p1)/2
    @staticmethod
    def millieustatic(p1,p2):
        return (math.sqrt((p1.__x - p2.__x) ** 2 + (p1.__y - p2.__y) ** 2))/2
    def plusProche(self,other):
        p = Point(0,0)
        if self.distance(p)>other.distance(p):
            return other.afficher()
        else:
            return self.afficher()
        # a = self.x
        # b=self.y
        # c=other.x
        # d=other.y
        # if self.x<0:
        #     self.x*=-1
        # if self.y<0:
        #     self.y*=-1
        # if other.x<0:
        #     other.x*=-1
        # if other.y<0:
        #     other.y*=-1
        # if (self.x<other.x):
        #     return f"({a},{b})"
        # else:
        #     return f"({c},{d})"

class Cercle:

    def __init__(self,rayon,centre = Point(0,0)):
        self.rayon=rayon
        self.centre=centre
    def __str__(self):
        return f"le rayon est:{self.rayon} et le centre ({self.centre.getX()},{self.centre.getY()})"
    def  deplacer(self,dx,dy):
        self.centre.setX(self.centre.getX()+dx)
        self.centre.setY(self.centre.getY()+dy)
    def setRoyon(self,r):
        self.rayon=r
    def surface(self):
        return (math.pi)*(self.rayon**2)
    def circonferonce(self):
        return 2*math.pi*self.rayon


p1 = Point(1,4)
c1 = Cercle(5,p1)
print(c1)


