import csv
reader = csv.DictReader(open("eleves.csv", "r"))
classe = []
for row in reader:
    classe.append(dict(row))
print(classe)

moyenneClasse = []


def moyenne(eleve):
    moy = (int(eleve["Programmation"])+ int(eleve["Algorithmique"])+ int(eleve["Projet"]))/3
    moyenneClasse.append(moy)
    return moy

def moyenneProgrammation(classe):
    moyProg = 0
    for i in range(0, 3):
        moyProg += int(classe[i]["Programmation"])
    return moyProg/3

def moyenneAlgorithmique(classe):
    moyAlgo = 0
    for i in range(0, 3):
        moyAlgo += int(classe[i]["Algorithmique"])
    return moyAlgo/3

def moyenneProjet(classe):
    moyProjet = 0
    for i in range(0, 3):
        moyProjet += int(classe[i]["Projet"])
    return moyProjet/3

def moyenneGenerale(classe):
    moyG = 0
    for i in range(0, 3):
        moyG += classe[i]
    return moyG/3

for i in range(0, 3):
    print("moyenne de", classe[i]["Prenom"], ":", moyenne(classe[i]))

print("moyenne de la classe : ", moyenneGenerale(moyenneClasse))
print("moyenne de : Programmation: ", moyenneProgrammation(classe))
print("moyenne de : Algorithmique: ", moyenneAlgorithmique(classe))
print("moyenne de : Projet: ", moyenneProjet(classe))