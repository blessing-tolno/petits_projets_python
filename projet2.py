# La mini calculatrice

print("Choisir entre ces opérateurs et écrire comme tel :\
     soustraction--addition--multiplication--division--reste ")
operateur = input("Quelle opérateur souhaiter vous utilisez? ")
nbre1 = int(input("Entrer le premier nombre "))
nbre2 = int(input("Entrer le deuxième nombre "))

if operateur == "soustraction":
    print(f"La difference est : {nbre1 - nbre2} ")
elif operateur == "addition" :
    print(f"La somme est : {nbre1 + nbre2} ")
elif operateur == "multiplication" :
    print(f"La multiplication est : {nbre1 * nbre2} ")
elif operateur == "division" :
    print(f"La division est : {nbre1 /  nbre2} ")
else :
    print(f"Le reste de la division est :  {nbre1 % nbre2} ")