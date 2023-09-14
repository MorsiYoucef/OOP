class Employee:
    def __init__(self,__id,__nom):
        self.__id=__id
        self.__nom=__nom
        # if self.__id <= 100:
        #     self.__id += 1
    def __str__(self):
        return f"ID :{self.__id} Nom :{self.__nom}"

    def setID(self,id):
        self.__id=id
    def getID(self):
        return self.__id
    def setNom(self,nom):
        self.__nom=nom
    def getNom(self):
        return self.__nom
class Agent(Employee):
    def __init__(self,id,nom,salaire=30000):
        super().__init__(id,nom)
        self.salaire = salaire
    def Salaire(self):
        return self.salaire
    def __str__(self):
        return f"ID :{self.getID()} Nom :{self.getNom()} Categorie :Agent ,Salaire :{self.salaire}"
class Ingenieur(Employee):
    def __init__(self,id,nom,heure_supp,salaire=45000,prim_Docu=600):
        super().__init__(id,nom)
        self.salaire = salaire
        self.Prim_Docu=prim_Docu
        self.heure_supp=heure_supp
    def Salaire(self):
        return self.salaire+(self.heure_supp*self.Prim_Docu)
    def __str__(self):
        return f"ID :{self.getID()} Nom :{self.getNom()} Categorie :Igenieur ,Salaire :{self.Salaire()} "
class CadreSup(Employee):
    def __init__(self,id,nom,heure_supp,salaire=60000,prim_Docu=1200):
        super().__init__(id,nom)
        self.salaire = salaire
        self.Prim_Docu=prim_Docu
        self.heure_supp=heure_supp
    def Salaire(self):
        return self.salaire+(self.heure_supp*self.Prim_Docu)
    def __str__(self):
        return f"ID :{self.getID()} Nom :{self.getNom()} Categorie :Igenieur ,Salaire :{self.Salaire()} "

class Personne:
    listof = []

    def ajouterEmp(self,E = Employee):

        self.listof.append(E)
    def afficher(self):
        for insetance in self.listof:
            print(insetance.__str__())
    def SalaireMoyen(self):
        m=0
        for insetance in self.listof:
            m+=insetance.Salaire()
        return m/len(self.listof)
    def SalaireMoyenIng(self):
        m=0
        s=0
        for insetance in self.listof:
            if insetance.salaire==45000:
              s += 1
              m+=insetance.Salaire()
        if s == 0: return 0
        else: return m/s





p = Personne()
E1 = Agent(1,"omar")
E2 = Ingenieur(2,"yusuf",50)
E3 = CadreSup(3,"lotfi",35)
E4 = Ingenieur(4,"mohammed",15)
# print(E1)
# print(E2)
# print(E3)
p.ajouterEmp(E1)
p.ajouterEmp(E2)
p.ajouterEmp(E3)
p.ajouterEmp(E4)

p.afficher()
print(p.SalaireMoyen())
print(p.SalaireMoyenIng())
