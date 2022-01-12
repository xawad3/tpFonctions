from mesfonctions import *
from datetime import date


print("Il y a un nouveau joueur de quidditch ? Dites nous tout !")
print("——————————————————————————————————————————————————————————")

#inscrits = int(input("indiquez le nombre de personnes à inscrire\n"))


#for i in range (inscrits):
leslistes = {"poussins":[],"cadets":[],"junior":[],"semipro": [],"pro":[]}


inscrire = True
while inscrire:


    inscription = {}
    inscription["nom"] = input("Ecrivez le nom\n")
    inscription["prenom"] = input("Ecrivez le prénom\n")
    continuer = True
    while continuer:
        inscription["year"] = input("Ecrivez année de naissance\n")
        try:
            inscription["year"] = int(inscription["year"])
        except ValueError:
            print("veuillez indiquer l'année en chiffres")
        else:
            continuer = False


    email = Mail(inscription["nom"][0], inscription["prenom"])
    inscription["email"] = email

    if 6 <= age(inscription["year"]) < 12:
        leslistes["poussins"].append(inscription)
    elif 12 <= age(inscription["year"]) < 18:
        leslistes["cadets"].append(inscription)
    elif 18 <= age(inscription["year"]) < 24:
        leslistes["junior"].append(inscription)
    elif 24 <= age(inscription["year"]) < 30:
        leslistes["semipro"].append(inscription)
    elif 30 <= age(inscription["year"]) <= 40:
        leslistes["pro"].append(inscription)
    else:
        print("NON ADMIS")

    date_ = str(date.today())
    create_csv("inscrits-" + date_ + ".csv", leslistes)


    ok = input("il y a t-il encore une entrée, o/n ?")
    if ok == "o":
        inscrire = True

    else:
        inscrire = False



print("Voici les nouveaux inscrits:")
print(leslistes)