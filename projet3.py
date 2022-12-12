import random
# Jeu Devine le Nombre (Ordinateur donne un nombre aléatoire dans un interval qu'on aura choisi
# Puis à nous de déviner le nombre de l'ordinateur)

# Nous allons apprendre comment utiliser le module random de Python, 
# créer des fonctions, travailler avec la boucle while et les conditionnels, 
# et récupérer les entrées de l'utilisateur.

# Créeation de la fonction deviner()
def deviner(x):
    # Déclaration de la variable qui contiendra le nombre le nombre choisi par l'ordinateur
    random_nombre = random.randint(1,x)
    deviner = 0
    while deviner != random_nombre:
        deviner = int(input(f'Déviner un nombre entre 1 et {x} '))
        if deviner < random_nombre:
            print("Désoler! Déviner encore. c'est bas ")
        elif deviner > random_nombre:
            print("Désoler! Déviner encore. c'est haut")
        
    print(f"Ouais! Félicitation. Tu as déviner le nombre {random_nombre} correctements ")

deviner(10)