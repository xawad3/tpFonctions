from mesfonctions import *

poussin = []
cadet = []
junior = []
semipro = []
pro = []


inscription = {}
inscription["nom"] = input("Ecrivez le nom\n")
inscription["prenom"] = input("Ecrivez le prénom\n")
inscription["year"] = int(input("Ecrivez année de naissance\n"))

email = Mail(inscription["nom"][0],inscription["prenom"])


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




print(email)
print(poussin)
print(age(inscription["year"]))





