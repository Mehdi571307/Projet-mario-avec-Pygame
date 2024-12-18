fichier = r"C:\Users\stagiaire\Downloads\level7_data.txt"

lignes = []  # future liste des lignes
with open(fichier, "rb") as f:
    for ligne in f:
        ligne = ligne.rstrip()  # supprime les octets de fin de ligne
        try:
            # Essayer de décoder les octets en UTF-8
            ligne = ligne.decode("utf-8")
        except UnicodeDecodeError:
            print("Erreur de décodage pour cette ligne.")
        lignes.append(ligne)  # ajoute la ligne décodée à la liste
        print(ligne)  # affiche la ligne décodée

# Pas besoin de fermer le fichier: c'est fait automatiquement avec 'with'

