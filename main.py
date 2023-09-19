def compter_mots(chaine):
    # split() permet de separer une phrase en chaines de characteres en les separant par un espace (whitespace)
    # on utilise donc le chaine (ce que on met sur la fonction) et on le split()
    mots = chaine.split()

    # on utlise la fonction len() pour compter le nombre de chaines de characteres qu'on a dans le chaine.split()
    nombre_de_mots = len(mots)

    print("Le nombre de mots dans la chaine est :", nombre_de_mots)
# alors, on utilise la fonction sur ce que l'utilisateur met comme input
chaine_de_caracteres = input("Met des chaines de characteres et je vais compter combien il y en a.")
compter_mots(chaine_de_caracteres)
