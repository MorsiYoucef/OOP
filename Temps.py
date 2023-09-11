class Temps:

    def __init__(self, heurs,minutes,secondes):
        self.heurs=heurs
        self.minutes=minutes
        self.secondes=secondes
    def __int__(self,heurs=0,minutes=0,secondes=0):
        pass

    def PlusGrand(self,T):
        return (self.heurs>T.heurs or (self.heurs==T.heurs and self.minutes>T.minutes)or (self.heurs==T.heurs and self.minutes==T.minutes and self.secondes>T.secondes))

    def diffTemp(self,T):
        dh=0
        ds=0
        dm=0
        if (self.heurs>T.heurs):
            dh = self.heurs-T.heurs
        else:
            dh= T.heurs-self.heurs

        if (self.minutes > T.minutes):
            dm = self.minutes - T.minutes
        else:
            dm = T.minutes - self.minutes

        if (self.secondes > T.secondes):
            ds = self.secondes - T.secondes
        else:
            ds = T.secondes - self.secondes

        return f"{dh}h:{dm}m:{ds}s"

T1 = Temps(45,45,5)
T2 = Temps(12,59,30)
print(Temps.PlusGrand(T1,T2))
print(Temps.diffTemp(T1,T2))




