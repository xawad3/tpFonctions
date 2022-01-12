import csv

def age(annee):
    return 2022-annee

def Mail(first_letter, prenom):
    mailtemplate = "@baton-rouge.fr"
    mail = ""
    mail += first_letter.upper()
    mail += "."
    mail += prenom.lower()
    mail += mailtemplate

    return mail

def create_csv(fichier,leslistes):
    with open(fichier, "w", newline="") as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=" ")
        for i in leslistes:
            for j in leslistes[i]:
                utilisateur = []
                for k in j:
                    utilisateur.append(str(j[k]))
                spamwriter.writerow([utilisateur[0], utilisateur[1], utilisateur[2], utilisateur[3], i])