import math
class Point:
    def __init__(self,x=0,y=None):
        if y is None:
            y = x
        self.x = x
        self.y = y
    def afficher(self):
        return f"({self.x},{self.y})"
    def deplacer(self,dx,dy):
        self.x+=dx
        self.y+=dy
    def distance(self,other):
        return math.sqrt((self.x-other.x)**2 + (self.y-other.y)**2)

    def millieu(self):
        return self.distance(other=p2)/2
    @staticmethod
    def millieustatic(p1,p2):
        return (math.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2))/2
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


p1 = Point(4,4)
p2 = Point(-1,4)
print(p1.afficher())
# p1.deplacer(1,1)

print(Point.distance(p1,p2))
print(p1.millieu())
print(Point.millieustatic(p1,p2))
print(Point.plusProche(p1,p2))
