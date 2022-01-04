inscription = {}
inscription["nom"] = input("Ecrivez le nom")
inscription["prenom"] = input("Ecrivez le prénom")
inscription["year"] = int(input("Ecrivez année de naissance"))

poussin = []
cadet = []
junior = []
semipro = []
pro = []



def age(annee):
    return 2022-annee


if age(inscription["year"]) < 18:
    poussin.append(inscription)

print(poussin)
print(age(inscription["year"]))


#print(inscription)

#print(inscription["year"])


