from tkinter import *
from G8class import *
SelectBiere = False
SelectVin = False
PrixBouteille = False #Si prix bouteille, false si prix verre
PrixLieu = 0 #Si sur place, 1 si à emporter
from copy import *
FiltrePlus = []

def CheckbuttonsCouleur(Checkbt):
    global Moteur, CouleurRose, CouleurBlanc, CouleurRouge, CouleurBiere, SelectBiere, TypeBiereBlonde, TypeBiereBrune, TypeBiereBlanche, TypeBiereIPA, SelectVin, ErreurCritere, TypeVin, TypeBiere
    try:ErreurCritere.destroy()
    except:pass
    select = {CouleurRose : "Rosé", CouleurBlanc : "Blanc", CouleurRouge : "Rouge"}
    for k in [CouleurRose, CouleurBlanc, CouleurRouge, CouleurBiere]:
        if k != Checkbt:
            k.deselect()

            if k == CouleurBiere and SelectBiere :
                TypeBiereBlonde.destroy()
                TypeBiereBrune.destroy()
                TypeBiereBlanche.destroy()
                TypeBiereIPA.destroy()

    if Checkbt == CouleurBiere and SelectBiere == False:
        SelectVin = False
        SelectBiere = True
        TypeBiereBlonde = Checkbutton(Moteur, text = "Blonde", command = lambda: CheckbuttonsBiere(TypeBiereBlonde))
        TypeBiereBlonde.grid(row = 4, column = 1)
        TypeBiereBlanche = Checkbutton(Moteur, text = "Blanche", command = lambda: CheckbuttonsBiere(TypeBiereBlanche))
        TypeBiereBlanche.grid(row = 4, column = 0)
        TypeBiereBlanche.select()
        TypeBiere = "Blanche"
        TypeBiereBrune = Checkbutton(Moteur, text = "Brune/Ambrée".encode('utf8'), command = lambda: CheckbuttonsBiere(TypeBiereBrune))
        TypeBiereBrune.grid(row = 4, column = 2)
        TypeBiereIPA = Checkbutton(Moteur, text = "IPA", command = lambda: CheckbuttonsBiere(TypeBiereIPA))
        TypeBiereIPA.grid(row = 4, column = 3)
    elif Checkbt == CouleurBiere and SelectBiere == True :
        SelectVin = False
        SelectBiere = False
        TypeBiereBlonde.destroy()
        TypeBiereBrune.destroy()
        TypeBiereBlanche.destroy()
        TypeBiereIPA.destroy()
    else :
        if SelectVin:
            SelectVi = False
        else:
            SelectVin = True
            TypeVin = select[Checkbt]


def CheckbuttonsBiere(Checkbt):
    global TypeBiereBlonde, TypeBiereBrune, TypeBiereBlanche, ErreurCritere, TypeBiere
    try:ErreurCritere.destroy()
    except:pass
    select = {TypeBiereBlonde : "Blonde", TypeBiereBrune : "Brune", TypeBiereBlanche : "Blanche"}
    for k in [TypeBiereBlonde, TypeBiereBrune, TypeBiereBlanche, TypeBiereIPA]:
        if k != Checkbt :
            k.deselect()
        TypeBiere =select[Checkbt]

def CheckbuttonsPrix(Checkbt):
    global AuVerre, ALaBouteille, PrixBouteille, PrixLieu, SurPlace
    if PrixLieu == 1 and Checkbt == AuVerre:
        SurPlace.invoke()
    if PrixBouteille:
        A=1
    else:
        A=0

    if Checkbt == AuVerre :
        A = abs(A-1)
        ALaBouteille.toggle()
    else:
        A = abs(A-1)
        AuVerre.toggle()

    PrixBouteille = (A == 1)

def CheckbuttonsLieu(Checkbt):
    global SurPlace, AEmporter, PrixLieu, PrixBouteille, ALaBouteille
    if Checkbt == AEmporter :
        PrixLieu = abs(PrixLieu-1)
        SurPlace.toggle()
        if PrixBouteille == False:
            ALaBouteille.invoke()
    else:
        PrixLieu = abs(PrixLieu-1)
        AEmporter.toggle()


def AfficheCriteres():
    global Param, Moteur, SelectVin, SelectBiere, Criteres, Param, Recherche, Boutons, FiltrePlus, ErreurCritere
    FiltrePlus = []
    Param.destroy()

    if SelectVin :
        try:ErreurCritere.destroy()
        except:pass
        Criteres = ["Fin","Délicat","Fruité","Souple","Marqué","Riche","Boisé","Voluptueux","Sec","Vif","Acide","Ample","Exotique","Floral","Rond","Mature","Soyeux","Epicé","Frais","Racé","Dense","Puissant","Corsé","Minéral","Structuré","Tanis","Gourmand","Charnu","Equilibré"]
        Criteres.sort()
        Boutons = []
        Coords = [(5,0),(5,1),(5,2),(5,3),(5,4),(5,5),(5,6),(5,7),(6,0),(6,1),(6,2),(6,3),(6,4),(6,5),(6,6),(7,0),(7,1),(7,2),(7,3),(7,4),(7,5),(7,6),(7,7),(8,0),(8,1),(8,2),(8,3),(8,4),(8,5),(8,6),]
        Bt0 = Checkbutton(Moteur, text = "Acide", command = lambda:Filtrage("Acide"))
        Bt0.grid(row = 5, column = 0, sticky = "nw")
        Boutons.append(Bt0)
        Bt1 = Checkbutton(Moteur, text = "Ample", command = lambda:Filtrage("Ample"))
        Bt1.grid(row = 5, column = 1, sticky = "nw")
        Boutons.append(Bt1)
        Bt2 = Checkbutton(Moteur, text = "Boisé" , command = lambda:Filtrage("Boisé"))
        Bt2.grid(row = 5, column = 2, sticky = "nw")
        Boutons.append(Bt2)
        Bt3 = Checkbutton(Moteur, text = "Charnu", command = lambda:Filtrage("Charnu"))
        Bt3.grid(row = 5, column = 3, sticky = "nw")
        Boutons.append(Bt3)
        Bt4 = Checkbutton(Moteur, text = "Corsé" , command = lambda:Filtrage("Corsé"))
        Bt4.grid(row = 5, column = 4, sticky = "nw")
        Boutons.append(Bt4)
        Bt5 = Checkbutton(Moteur, text = "Dense", command = lambda:Filtrage("Dense"))
        Bt5.grid(row = 5, column = 5, sticky = "nw")
        Boutons.append(Bt5)
        Bt6 = Checkbutton(Moteur, text = "Délicat" , command = lambda:Filtrage("Délicat"))
        Bt6.grid(row = 5, column = 6, sticky = "nw")
        Boutons.append(Bt6)
        Bt7 = Checkbutton(Moteur, text = "Epicé" , command = lambda:Filtrage("Epicé"))
        Bt7.grid(row = 5, column = 7, sticky = "nw")
        Boutons.append(Bt7)
        Bt8 = Checkbutton(Moteur, text = "Equilibré" , command = lambda:Filtrage("Equilibré"))
        Bt8.grid(row = 6, column = 0, sticky = "nw")
        Boutons.append(Bt8)
        Bt9 = Checkbutton(Moteur, text = "Exotique", command = lambda:Filtrage("Exotique"))
        Bt9.grid(row = 6, column = 1, sticky = "nw")
        Boutons.append(Bt9)
        Bt10 = Checkbutton(Moteur, text = "Fin", command = lambda:Filtrage("Fin"))
        Bt10.grid(row = 6, column = 2, sticky = "nw")
        Boutons.append(Bt10)
        Bt11 = Checkbutton(Moteur, text = "Floral", command = lambda:Filtrage("Floral"))
        Bt11.grid(row = 6, column = 3, sticky = "nw")
        Boutons.append(Bt11)
        Bt12 = Checkbutton(Moteur, text = "Frais", command = lambda:Filtrage("Frais"))
        Bt12.grid(row = 6, column = 4, sticky = "nw")
        Boutons.append(Bt12)
        Bt13 = Checkbutton(Moteur, text = "Fruité" , command = lambda:Filtrage("Fruité"))
        Bt13.grid(row = 6, column = 5, sticky = "nw")
        Boutons.append(Bt13)
        Bt14 = Checkbutton(Moteur, text = "Gourmand", command = lambda:Filtrage("Gourmand"))
        Bt14.grid(row = 6, column = 6, sticky = "nw")
        Boutons.append(Bt14)
        Bt15 = Checkbutton(Moteur, text = "Marqué" , command = lambda:Filtrage("Marqué"))
        Bt15.grid(row = 7, column = 0, sticky = "nw")
        Boutons.append(Bt15)
        Bt16 = Checkbutton(Moteur, text = "Mature", command = lambda:Filtrage("Mature"))
        Bt16.grid(row = 7, column = 1, sticky = "nw")
        Boutons.append(Bt16)
        Bt17 = Checkbutton(Moteur, text = "Minéral" , command = lambda:Filtrage("Minéral"))
        Bt17.grid(row = 7, column = 2, sticky = "nw")
        Boutons.append(Bt17)
        Bt18 = Checkbutton(Moteur, text = "Puissant", command = lambda:Filtrage("Puissant"))
        Bt18.grid(row = 7, column = 3, sticky = "nw")
        Boutons.append(Bt18)
        Bt19 = Checkbutton(Moteur, text = "Racé" , command = lambda:Filtrage("Racé"))
        Bt19.grid(row = 7, column = 4, sticky = "nw")
        Boutons.append(Bt19)
        Bt20 = Checkbutton(Moteur, text = "Riche", command = lambda:Filtrage("Riche"))
        Bt20.grid(row = 7, column = 5, sticky = "nw")
        Boutons.append(Bt20)
        Bt21 = Checkbutton(Moteur, text = "Rond", command = lambda:Filtrage("Rond"))
        Bt21.grid(row = 7, column = 6, sticky = "nw")
        Boutons.append(Bt21)
        Bt22 = Checkbutton(Moteur, text = "Sec", command = lambda:Filtrage("Sec"))
        Bt22.grid(row = 7, column = 7, sticky = "nw")
        Boutons.append(Bt22)
        Bt23 = Checkbutton(Moteur, text = "Souple", command = lambda:Filtrage("Souple"))
        Bt23.grid(row = 8, column = 0, sticky = "nw")
        Boutons.append(Bt23)
        Bt24 = Checkbutton(Moteur, text = "Soyeux", command = lambda:Filtrage("Soyeux"))
        Bt24.grid(row = 8, column = 1, sticky = "nw")
        Boutons.append(Bt24)
        Bt25 = Checkbutton(Moteur, text = "Structuré" , command = lambda:Filtrage("Structuré"))
        Bt25.grid(row = 8, column = 2, sticky = "nw")
        Boutons.append(Bt25)
        Bt26 = Checkbutton(Moteur, text = "Tanis", command = lambda:Filtrage("Tanis"))
        Bt26.grid(row = 8, column = 3, sticky = "nw")
        Boutons.append(Bt26)
        Bt27 = Checkbutton(Moteur, text = "Vif", command = lambda:Filtrage("Vif"))
        Bt27.grid(row = 8, column = 4, sticky = "nw")
        Boutons.append(Bt27)
        Bt28 = Checkbutton(Moteur, text = "Voluptueux", command = lambda:Filtrage("Voluptueux"))
        Bt28.grid(row = 8, column = 5, sticky = "nw")
        Boutons.append(Bt28)
            #TODO : implémenter à la main chaque bouton






        Param = Button(Moteur, text = "Cacher les critères" , command = CacherCriteres)
        Param.grid(row = 9, column = 0, columnspan = 3)
        Recherche.grid(row = 9, column = 3, columnspan = 5)


    elif SelectBiere :
        try:ErreurCritere.destroy()
        except:pass
        Criteres = ["Fruitée","Bulles fines","Bulles vives"]
        Boutons = []
        Coords = [(5,0),(5,1),(5,2)]
        Bt0 = Checkbutton(Moteur, text = "Fruitée" , command = lambda:Filtrage("Fruitée"))
        Bt0.grid(row = 5, column = 0)
        Boutons.append(Bt0)
        Bt1 = Checkbutton(Moteur, text = "Bulles fines", command = lambda:Filtrage("Bulles fines"))
        Bt1.grid(row = 5, column = 1)
        Boutons.append(Bt1)
        Bt2 = Checkbutton(Moteur, text = "Bulles vives", command = lambda:Filtrage("Bulles vives"))
        Bt2.grid(row = 5, column = 2)
        Boutons.append(Bt2)

            #TODO : implémenter à la main chaque bouton




        Param = Button(Moteur, text = "Cacher les critères" , command = CacherCriteres)
        Param.grid(row = 6, column = 0, columnspan = 3)
        Recherche.grid(row = 6, column = 3, columnspan = 5)

    else :
        ErreurCritere = Label(Moteur,text="Veuillez selectionner un type de boisson",bg = "red")
        ErreurCritere.grid(row = 6, column = 0, columnspan = 3)
        Param = Button(Moteur, text = "Plus de critères" , command = AfficheCriteres)
        Param.grid(row = 5, column = 0, columnspan = 3)


def Filtrage(crit):
    global FiltrePlus, Criteres
    if crit in FiltrePlus:
        FiltrePlus.remove(crit)
    else:
        FiltrePlus.append(crit)
    # print(FiltrePlus)

def CacherCriteres():
    global Moteur, Criteres, Param, Recherche, Boutons, FiltrePlus
    Param.destroy()
    Recherche.destroy()
    Criteres = []
    FiltrePlus = []
    for k in Boutons :
        try: k.destroy()
        except: pass
    Param = Button(Moteur, text = "Plus de critères" , command = AfficheCriteres)
    Param.grid(row = 5, column = 0, columnspan = 3)

    Recherche = Button(Moteur, text = "Chercher", command = Chercher)
    Recherche.grid(row = 5, column = 3, columnspan = 5)







def Chercher():
    global Moteur, PrixMin, PrixMax, TypeVin, TypeBiere, Barre, FiltrePlus, PrixBouteille, SelectBiere, SelectVin, FiltrePlus, PrixLieu



    TropLong = False
    if SelectBiere:
        Typeb = TypeBiere
    elif SelectVin:
        Typeb = TypeVin
    else:
        Typeb = None


    Texte = Barre.get()
    PMin = PrixMin.get()
    if PMin == "":
        PMin = 0
    else:
        PMin = float(PMin)
    PMax = PrixMax.get()
    if PMax == "":
        PMax = 10000
    else:
        PMax = float(PMax)


    Widgets = Moteur.winfo_children()
    for k in Widgets:
        try :
            k.destroy()
        except :
            pass

    Attente = Label(Moteur,text="Recherche...")
    Attente.grid(row = 0, column = 0)

    ResultatsInit = deepcopy(BoissonsG8)
    ResultatsFin = []
    for boiss in ResultatsInit:

        if not(Texte in boiss.name):
            # print("nom")
            continue

        if Typeb != None:
            if not(Typeb in boiss.type):
                # print("type")
                continue

        if PrixBouteille:
            if PMax < boiss.bouteille[PrixLieu] or PMin > boiss.bouteille[PrixLieu] or boiss.bouteille[PrixLieu] == 0:
                # print("prixb")
                continue
        else:
            if PMax < boiss.glass[PrixLieu] or PMin > boiss.glass[PrixLieu] or boiss.glass[PrixLieu] == 0:
                # print("prixv")
                continue

        for crit in FiltrePlus :
            if not(crit in boiss.crit):
                # print("crit")
                continue

        ResultatsFin.append(boiss)
    Attente.destroy()
    AfficherPage(1,ResultatsFin)


def AfficherPage(Page,Liste):
    global Moteur

    Widgets = Moteur.winfo_children()
    for k in Widgets:
        try :
            k.destroy()
        except :
            pass

    Colonnes = ["Nom","Type","Prix Verre","Prix Bouteille"]
    Page -= 1
    Liste2 = Liste[Page*10:min(Page*10+10,len(Liste))]
    for k in range(len(Colonnes)):
        L = Label(Moteur, text = Colonnes[k])
        L.grid(row = 0, column = k)
    for k in range(len(Liste2)) :
        boiss = Liste2[k]
        L1 = Label(Moteur, text = str(boiss.name))
        L1.grid(row = k+1, column = 0)
        t=""
        for c in boiss.type:
            t += c
            t += ","
        L2 = Label(Moteur, text = t[:-1])
        L2.grid(row = k+1, column = 1)
        if boiss.glass[PrixLieu]>0:
            P1 = str(round(boiss.glass[PrixLieu],2))+"€"
        else:
            P1 = "X"
        L3 = Label(Moteur, text = P1)
        L3.grid(row = k+1, column = 2)
        if boiss.bouteille[PrixLieu]>0:
            P2 = str(round(boiss.bouteille[PrixLieu],2))+"€"
        else:
            P2 = "X"
        L4 = Label(Moteur, text = P2)
        L4.grid(row = k+1, column = 3)
    if len(Liste) == 0:
        Triste = label(Moteur, text = "Aucun élément ne correspond à votre recherche.")
        Triste.grid(row = 5, column = 0, columnspan = 4)
    if Page>0:
        PagePrec = Button(Moteur, text = "Page précédente", command = lambda : AfficherPage(Page,Liste))
        PagePrec.grid(row = k+2, column = 0, sticky = "nw")
    if (Page+1)*10<len(Liste):
        PageSuiv = Button(Moteur, text = "Page suivante", command = lambda : AfficherPage(Page+2,Liste))
        PageSuiv.grid(row = k+2, column = 3, sticky = "ne")

    Accueil = Button(Moteur, text = "Retour à l'accueil", command = Depart)
    Accueil.grid(row = k+3, column = 0, columnspan = 4)






















def Depart():
    global Moteur, Param, Recherche, PrixMax, PrixMin, Barre, AuVerre, ALaBouteille, CouleurBiere, CouleurBlanc, CouleurRose, CouleurRouge, AEmporter, SurPlace

    Widgets = Moteur.winfo_children()
    for k in Widgets:
        try :
            k.destroy()
        except :
            pass

    LabBarre = Label(Moteur,text = "Nom :")
    LabBarre.grid(row = 0,column = 0, columnspan = 4)
    Barre = Entry(Moteur, width = 30) #TODO : Entry
    Barre.grid(row = 1,column = 0, columnspan = 4)

    LabCouleur = Label(Moteur, text = "Couleur")
    LabCouleur.grid(row = 2, column = 0, columnspan = 4)
    CouleurRose = Checkbutton(Moteur, text = "Rosé", command = lambda: CheckbuttonsCouleur(CouleurRose))
    CouleurRose.grid(row = 3, column = 0)
    CouleurBlanc = Checkbutton(Moteur, text = "Blanc", command = lambda: CheckbuttonsCouleur(CouleurBlanc))
    CouleurBlanc.grid(row = 3, column = 1)
    CouleurRouge = Checkbutton(Moteur, text = "Rouge", command = lambda: CheckbuttonsCouleur(CouleurRouge))
    CouleurRouge.grid(row = 3, column = 2)
    CouleurBiere = Checkbutton(Moteur, text = "Bière", command = lambda: CheckbuttonsCouleur(CouleurBiere))
    CouleurBiere.grid(row = 3, column = 3)

    LabPrixMin = Label(Moteur, text = "Prix min :")
    LabPrixMin.grid(row = 0, column = 4)
    PrixMin = Entry(Moteur, width = 3)   #TODO : Entry
    PrixMin.grid(row = 0, column = 5)
    LabPrixMax = Label(Moteur, text = "Prix max :")
    LabPrixMax.grid(row = 1, column = 4)
    PrixMax = Entry(Moteur, width = 3)   #TODO : Entry
    PrixMax.grid(row = 1, column = 5)

    AuVerre = Checkbutton(Moteur, text = "Au verre", command= lambda : CheckbuttonsPrix(AuVerre))
    AuVerre.grid(row = 0, column = 6, sticky='nw')
    AuVerre.select()
    ALaBouteille = Checkbutton(Moteur, text = "A la bouteille", command= lambda : CheckbuttonsPrix(ALaBouteille))
    ALaBouteille.grid(row = 1, column = 6, sticky='nw')

    SurPlace = Checkbutton(Moteur, text = "Sur place", command= lambda : CheckbuttonsLieu(SurPlace))
    SurPlace.grid(row = 0, column = 7, sticky='nw')
    SurPlace.select()
    AEmporter = Checkbutton(Moteur, text = "A emporter", command= lambda : CheckbuttonsLieu(AEmporter))
    AEmporter.grid(row = 1, column = 7, sticky='nw')


    Param = Button(Moteur, text = "Plus de critères", command = AfficheCriteres)
    Param.grid(row = 5, column = 0, columnspan = 3)

    Recherche = Button(Moteur, text = "Chercher", command = Chercher)
    Recherche.grid(row = 5, column = 3, columnspan = 5)


Moteur = Tk()
Moteur.title("Moteur de recherche")
Depart()
Moteur.mainloop()

#TODO : - Vérif PrixMin<PrixMax