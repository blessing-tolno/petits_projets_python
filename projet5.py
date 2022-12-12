import random
# Jeu pierre -- feuille -- ciseaux
# nous allons travailler avec random.choice le conditionnel if, 
# et récupérer les entrées provenant de l'utilisateur. Ceci est n bon projet pour nous aidez 
# à connaître les fondamentaux des conditionnels et des fonctions.
def play():
    user = input("Quel est ton chpoix : 'p' pour pierre, 'f' pour feuille, 'c' pour ciseaux\n")
    computer = random.choice(['p', 'f', 'c'])
    if user == computer :
        return 'Choix identique'

     # p > c, c > f, f > p
    if is_win(user, computer):
        return 'Tu as gangné'

    return 'Tu as perdu'

def is_win(player, opponent):
    # return True if player wins 
    # p > c, c > f, f > p
    if (player == 'p' and opponent== 'c') or (player == 'c' and opponent == 'f') or (player == 'f' and opponent == 'p'):
        return True

print(play())

