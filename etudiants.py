from niveau import *

class Etudiants(Niveau):
    def __init__(self, Nom, sexe, niveau):
        self.Nom = Nom
        self.sexe = sexe
        self.Niveau.Nom = niveau

students1 = Etudiants("Zogou", "Masculin", niveaul2)
students2 = Etudiants("Marie", "Feminin", niveaul3) 