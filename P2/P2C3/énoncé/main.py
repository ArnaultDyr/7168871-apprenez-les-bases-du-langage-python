# Ecrivez vos fonctions ici

def salaire_mensuel(salaire_annuel):
    return salaire_annuel/12

def salaire_hebdomadaire(salaire_mensuel):
    return salaire_mensuel/4

def salaire_horaire(salaire_hebdomadaire, heures_travaillees):
    return salaire_hebdomadaire/heures_travaillees

def main():
    salaire_annuel = input("Saississez votre salaire anuel : ")
    salaire_annuel = int(salaire_annuel)
    heures_travaillees = input("Saississez le nombre d'H travaillees : ")
    heures_travaillees = int(heures_travaillees)

    salaire = 0
    salaire = salaire_horaire( salaire_hebdomadaire(salaire_mensuel(salaire_annuel)) ,heures_travaillees)
    print(f"Votre salaire horaire est de {salaire} euros")

# Ne touchez pas le code ci-dessous
if __name__ == "__main__":
    main()