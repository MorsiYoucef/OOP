class Personne:
    def __init__(self,nom,prenom,date_naissance):
        self.__nom=nom
        self.__prenom=prenom
        self.date_naissance=date_naissance

    def getNom(self):
        return self.__nom

    def getPre(self):
        return self.__prenom
    def __str__(self):
        return f"nom :{self.__nom}, prenom :{self.__prenom} ,date-naissance :{self.date_naissance}"

class Employe(Personne):
    def __init__(self,nom,prenom,date_naissance,salaire):
        super().__init__(nom,prenom,date_naissance)
        self.__salaire=salaire
    def __str__(self):
        return super().__str__()+f"salaire :{self.__salaire}"
    def setSalaire(self,salaire):
        self.__salaire=salaire
    def getSalaire(self):
        return self.__salaire
class Directeur(Employe):
    def __init__(self,nom,prenom,date_naissance,salaire,societee):
        super().__init__(nom,prenom,date_naissance,salaire)
        self.societee=societee
    def __str__(self):
        return super().__str__()+f", societe :{self.societee}"
    def getSocietee(self):
        return self.societee
class Societee():
    listof= []
    s=0
    def __init__(self,NomSocietee,nbEmployer):
        self.NomSocietee=NomSocietee
        self.nbEmployer=nbEmployer
    def ajouter(self,p = Personne):

        if self.nbEmployer >= self.s+1 :
           self.listof.append(p)
           self.s+=1
    def afficher(self):
        for intec in self.listof:
            print(intec)

e1 = Employe("yusuf","Morsi","03-07-2003",80000)
e2 = Employe("lotfi","oukaci","22-10-2003",80000)
e3 = Employe("omar","debian","12-08-2003",65000)
e4 = Employe("djaafar","moulay","06-02-2000",100000)
e5 = Directeur("kamel","boudjaci","12-12-1990",150000,"Yassir")
S = Societee("Yassir",100)
S.ajouter(e1)
S.ajouter(e2)
S.ajouter(e3)
S.ajouter(e4)
S.ajouter(e5)
S.ajouter(e1)
S.ajouter(e1)
S.afficher()


        

