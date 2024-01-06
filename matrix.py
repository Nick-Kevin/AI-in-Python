def creer_matrice(nombre_lignes, nombre_colonne):
    Matrice = [[] for _ in range(nombre_lignes)]
    NumeroLigne = 1
    for Ligne in Matrice:
        print("Ligne " + str(NumeroLigne))
        NumeroColonne = 1
        for Column in range(nombre_colonne):
            ColumnValue = int(input("\tEntrez la valeur dans la colonne " + str(NumeroColonne) + ": "))
            Ligne.append(ColumnValue)
            NumeroColonne += 1
        NumeroLigne += 1
        
    return Matrice

Matrice = creer_matrice(3, 3)
print(Matrice)
