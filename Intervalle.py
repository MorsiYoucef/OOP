class Intervalle:
    # def __init__(self,BI :float,BS :float):
    #     self.BI=BI
    #     self.BS=BS

    def __init__(self,BI :float,BS :float):
        self.BI=BI
        self.BS=BS
        a=0
        #assert self.BI < self.BS
        if BI>BS:
            a=self.BI
            self.BI = self.BS
            self.BS=a
    def Largeur(self):
        return self.BS-self.BI
    def afficher(self):
        return f"[{self.BI},{self.BS}]"
    def millieu(self):
        return (self.BS+self.BI)/2
    def estAvant(self,other):
        if other.BI > self.BI:
            return True
        else:
            return False
    def estDisjoint(self,other):
        if other.BI>self.BS or self.BI>other.BS:
            return True
        else:
            return False
    def contient(self,point):
        if point> self.BI and point<self.BS:
            return True
        else:
            return False
    def estContenuDans(self,other):
        if self.BI<other.BI and self.BS>other.BS:
            return True
        else:
            return False
    def intersection(self,other):
        if self.estDisjoint(other)==True:
            return f"ya pas d'intersection!"
        if self.BI<other.BI and self.BS<other.BS:
            return f"[{other.BI},{self.BS}]"
        elif self.BI>other.BI and self.BS<other.BS:
            return f"[{self.BI},{other.BS}]"
        elif Intervalle.estContenuDans(self,other):
            return f"[{other.BI},{other.BS}]"
        elif Intervalle.estContenuDans(other,self):
            return f"[{self.BI},{self.BS}]"
    def intervPlusLarge(self,other):
        if self.Largeur()>other.Largeur():
            return f"[{self.BI},{self.BS}]"
        else:
            return f"[{other.BI},{other.BS}]"




i1 = Intervalle(1,12)
i2 = Intervalle(2,8)
print(i1.Largeur())
print(i1.afficher())
print(i1.millieu())
print(Intervalle.estAvant(i1,i2))
print(Intervalle.estDisjoint(i1,i2))
print(Intervalle.intersection(i1,i2))
print(Intervalle.intervPlusLarge(i1,i2))

