class PorteMonnaie:
    class Piece:
        def __init__(self, val, nbr):
            self.val = val
            self.nbr = nbr

        def get_val(self):
            return self.val

        def get_nbr(self):
            return self.nbr

        def set_nbr(self, nbr):
            self.nbr = nbr

    def __init__(self):
        self.tabPiece = [
            self.Piece(1, 0),
            self.Piece(5, 0),
            self.Piece(10, 0),
            self.Piece(20, 0),
            self.Piece(50, 0),
            self.Piece(100, 0),
            self.Piece(200, 0)
        ]

    def montant(self):
        m = 0
        for i in range(7):
            m += self.tabPiece[i].get_val() * self.tabPiece[i].get_nbr()
        return m

    def ajouter(self, dinars):
        self.tabPiece[0].set_nbr(self.tabPiece[0].get_nbr() + dinars)

    def ajouter_pieces(self, nbrUns, nbrCinq, nbrDix, nbrVingt, nbrCinquante, nbrCent, nbrDeuxCent):
        self.tabPiece[0].set_nbr(self.tabPiece[0].get_nbr() + nbrUns)
        self.tabPiece[1].set_nbr(self.tabPiece[1].get_nbr() + nbrCinq)
        self.tabPiece[2].set_nbr(self.tabPiece[2].get_nbr() + nbrDix)
        self.tabPiece[3].set_nbr(self.tabPiece[3].get_nbr() + nbrVingt)
        self.tabPiece[4].set_nbr(self.tabPiece[4].get_nbr() + nbrCinquante)
        self.tabPiece[5].set_nbr(self.tabPiece[5].get_nbr() + nbrCent)
        self.tabPiece[6].set_nbr(self.tabPiece[6].get_nbr() + nbrDeuxCent)

    def debourser(self, dinars):
        if self.montant() >= dinars:
            self.tabPiece[0].set_nbr(self.tabPiece[0].get_nbr() - dinars)
        self.optimiser_nbr_pieces()

    def optimiser_nbr_pieces(self):
        m = self.montant()

        self.tabPiece[6].set_nbr(m // 200)
        m %= 200
        self.tabPiece[5].set_nbr(m // 100)
        m %= 100
        self.tabPiece[4].set_nbr(m // 50)
        m %= 50
        self.tabPiece[3].set_nbr(m // 20)
        m %= 20
        self.tabPiece[2].set_nbr(m // 10)
        m %= 10
        self.tabPiece[1].set_nbr(m // 5)
        m %= 5
        self.tabPiece[0].set_nbr(m)

    def vider(self):
        for i in range(7):
            self.tabPiece[i].set_nbr(0)

    def __str__(self):
        result = ""
        for i in range(7):
            result += f"{self.tabPiece[i].get_nbr()} x {self.tabPiece[i].get_val()} da, "
        return result[:-2]

