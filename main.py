eleve1={"Nom":"Térieur","Prenom":"Alain","Date":"01/01/2000",
"Programmation":12,"Algorithmique":10,"Projet":15}

eleve2={"Nom":"Onette","Prenom":"Camille","Date":"01/07/2004",
"Programmation":7,"Algorithmique":14,"Projet":11}

eleve3={"Nom":"Oma","Prenom":"Modeste","Date":"01/11/2002",
"Programmation":13,"Algorithmique":8,"Projet":17}

classe = [eleve1, eleve2, eleve3]

moyenneClasse = []

def moyenne(eleve):
    moy = (eleve["Programmation"]+eleve["Algorithmique"]+eleve["Projet"])/3
    moyenneClasse.append(moy)
    return moy

def moyenneGenerale(classe):
    moyG = 0
    for i in range(0, 3):
        moyG += classe[i]
    return moyG/3

for i in range(0, 3):
    print("moyenne de", classe[i]["Prenom"], ":", moyenne(classe[i]))

print("moyenne de la classe : ", moyenneGenerale(moyenneClasse))