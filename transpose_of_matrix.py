from matrix import nombre_colonne, creer_matrice, afficher_matrice

def transpose(matrice):
    NombreDeColonnes = nombre_colonne(matrice)
    Transpose = [[] for _ in range(NombreDeColonnes)]    
    for LigneMatrice in matrice:
        NumeroColonne = 0
        for LigneTranspose in Transpose:
            LigneTranspose.append(LigneMatrice[NumeroColonne])
            NumeroColonne += 1
    return Transpose

def principal():
    NombreDeLigne = int(input("Entrez le nombre de lignes: "))
    NombreDeColonnes = int(input("Entrez le nombre de colonnes: "))
    print()
    Matrice = creer_matrice(NombreDeLigne, NombreDeColonnes)
    print("\n\nLa matrice")
    afficher_matrice(Matrice)
    Transpose = transpose(Matrice)
    print("\n\nTranspose de la matrice")
    afficher_matrice(Transpose)

principal()
