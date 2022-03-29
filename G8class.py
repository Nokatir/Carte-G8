from os import listdir
from io import open
class Boisson():

    def __init__(self,name):
        self.name = name

    def Criteres(self,liste):
        self.crit = []
        for c in liste:
            self.crit.append(c)
        self.crit.sort()

    def Type(self,typeb):
        self.type = typeb

    def Prix(self,PrixVerre,PrixBouteille):
        PrixVerre[0] = Check(PrixVerre[0])
        PrixVerre[1] = Check(PrixVerre[1])
        PrixBouteille[0] = Check(PrixBouteille[0])
        PrixBouteille[1] = Check(PrixBouteille[1])

        try:self.glass = (float(PrixVerre[0]), float(PrixVerre[1]))
        except:print(PrixVerre)
        self.bouteille = (float(PrixBouteille[0]), float(PrixBouteille[1]))

    def Fiche(self,fiche):
        self.fiche = fiche[:-4]+".pptx"

def Check(NumStr):
    if NumStr == "" or NumStr == "\n":
        NumStr = "0"
    return NumStr

BoissonsG8 = []
for fichier in listdir(r"Fiches"):
    Fiche = open("Fiches\\"+fichier,mode = "r", encoding="UTF-8")
    FicheL = Fiche.readlines()
    # print(FicheL)
    Nom = FicheL[0].strip()
    Type = (FicheL[1].strip()).split(",")
    PrixV = (FicheL[2].strip()).split(",")
    PrixB = (FicheL[3].strip()).split(",")
    Crits = (FicheL[4].strip()).split(",")
    B = Boisson(Nom)
    B.Criteres(Crits)
    B.Type(Type)
    B.Prix(PrixV,PrixB)
    B.Fiche("pptx\\"+fichier)
    BoissonsG8.append(B)