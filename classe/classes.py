class Eleve:
    '''
        Création d'une instance eleve:
        eleve=Eleve(nom(str),prenom(str),date(str),note1(programm)(float)
        ,note2(algo)(float),note3(projet(float)))
        attributs d'instance : nom,prenom,date,note_mat1,note_mat2,note_mat3
        attributs de classe: matiere1,matiere2,matiere3
        Méthode : moyenne() retourne la moyenne de l'élève
    '''

    matiere1 = "Programmation"
    matiere2 = "Algorithmique"
    matiere3 = "Projet"

    def __init__(self, Nom, Prenom, Date, Note1, Note2, Note3):
        self.nom=Nom
        self.prenom=Prenom
        self.date=Date
        self.note_mat1=Note1
        self.note_mat2=Note2
        self.note_mat3=Note3
    
    def moyenne(self):
        return (self.note_mat1 + self.note_mat2 + self.note_mat3)/3


eleve1 = Eleve("Térieur","Alain","01/01/2000",12,10,15)
eleve2 = Eleve("Onette","Camille","01/07/2004",7,14,11)
eleve3 = Eleve("Oma","Modeste","01/11/2002",13,8,17)

classe = [eleve1, eleve2, eleve3]
for i in range(0,3):
    print(classe[i].prenom,classe[i].nom)
    print(classe[i].matiere1,":",classe[i].note_mat1)
    print(classe[i].matiere2,":",classe[i].note_mat2)
    print(classe[i].matiere3,":",classe[i].note_mat3)
    print("Moyenne de ", classe[i].prenom,classe[i].nom, ":", classe[i].moyenne())

def moyenneParMatiere(classe):
    moyProg = 0
    moyAlgo = 0
    moyProjet = 0
    for i in range(0,3):
        moyProg += classe[i].note_mat1
        moyAlgo += classe[i].note_mat2
        moyProjet += classe[i].note_mat3
    return print("Programmation: ", moyProg/3, "Algo :", moyAlgo/3, "Projet: ",moyProjet/3)

moyenneParMatiere(classe)

help(Eleve)