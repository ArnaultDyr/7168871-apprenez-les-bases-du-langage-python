import csv

def main():
    with open("input.csv") as fichier_input:
        reader = csv.DictReader(fichier_input, delimiter=',')
        lignes = []
        for ligne in reader:
            lignes.append(ligne)
    with open("output.csv", 'w', newline='') as fichier_output:
        writer = csv.writer(fichier_output,delimiter=',')
        writer.writerow(['nom', 'salaire'])
        for ligne in lignes:
            salaire = 0
            salaire = int(ligne['heures_travaillees']) * 15
            writer.writerow([ligne['nom'], salaire])
           
        

# Ne touchez pas le code ci-dessous
if __name__ == "__main__":
    main()