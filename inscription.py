def age(annee):
    return 2022-annee

poussin = []
cadet = []
junior = []
semipro = []
pro = []
mailtemplate = "@baton-rouge.fr"
mail = ""
inscription = {}
inscription["nom"] = input("Ecrivez le nom")
inscription["prenom"] = input("Ecrivez le prénom")
inscription["year"] = int(input("Ecrivez année de naissance"))

firstLetter = inscription["nom"][0]
mail = ""
mail += firstLetter.upper()
mail += "."
secondLetter = inscription["prenom"]
mail += secondLetter.lower()
mail += mailtemplate


if 6 <= age(inscription["year"]) < 12:
    poussin.append(inscription)
elif 12 <= age(inscription["year"]) < 18:
    cadet.append(inscription)
elif 18 <= age(inscription["year"]) < 24:
    junior.append(inscription)
elif 24 <= age(inscription["year"]) < 30:
    semipro.append(inscription)
elif 30 <= age(inscription["year"]) <= 40:
    pro.append(inscription)
else:
    print("NON ADMIS")




print(mail)
print(poussin)
print(age(inscription["year"]))


#print(inscription)

#print(inscription["year"])


