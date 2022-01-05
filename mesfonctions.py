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