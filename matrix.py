def creer_matrice(nombre_lignes, nombre_colonne):
    Matrice = [[] for _ in range(nombre_lignes)]
    NumeroLigne = 1
    for Ligne in Matrice:
        print("Ligne " + str(NumeroLigne))
        NumeroColonne = 1
        for Colonne in range(nombre_colonne):
            ColumnValue = int(input("\tEntrez la valeur dans la colonne " + str(NumeroColonne) + ": "))
            Ligne.append(ColumnValue)
            NumeroColonne += 1
        NumeroLigne += 1
        
    return Matrice

def nombre_colonne(matrice):
    NombreDeColonnes = len(matrice[0])
    return NombreDeColonnes

def longueur_max_dans_une_colone(numero_colonne, matrice):
    LongueurMax = 1
    for Ligne in Matrix:
        Longueur = len(str(Ligne[numero_colonne]))
        if Longueur > LongueurMax:
            LongueurMax = Longueur
    return LongueurMax


def longueurs_max_des_colonnes(matrice):
    LongueursMax = []
    NombreDeColonnes = nombre_colonne(matrice)
    for numero_colonne in range(NombreDeColonnes):
        LongueurMaxDeLaColonne = longueur_max_dans_une_colone(numero_colonne, matrice)
        LongueursMax.append(LongueurMaxDeLaColonne)
    return LongueursMax

def afficher_une_valeur(longueur_max_colonne, valeur):
    AfficherValeur = ""
    space = " "
    LengthOfValue = len(str(valeur))
    NumberOfSpaces = longueur_max_colonne - LengthOfValue
    for i in range(NumberOfSpaces):
        AfficherValeur += space
    AfficherValeur += str(valeur)
    return AfficherValeur

def afficher_ligne(ligne, longueur_max_colonne):
    AfficherLigne = ""
    NumeroColonne = 0
    for Colonne in ligne:
        AfficherLigne += afficher_une_valeur(longueur_max_colonne[NumeroColonne], Colonne) + "  "
        NumeroColonne += 1
    return AfficherLigne

def afficher_matrice(matrice):
    LongueurMaxDesColonnes = longueurs_max_des_colonnes(matrice)
    for Ligne in matrice:
        print(afficher_ligne(Ligne, LongueurMaxDesColonnes))

Matrix = creer_matrice(3, 3)
afficher_matrice(Matrix)
