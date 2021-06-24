from Classes.PLayer import Player
from Classes.classes import Classes

print("Bonjour et bienvenu sur (titre du jeu pas encore trouver) voulez-vous connaitre les reglements du jeu? (oui/non)")
regle = input()
if regle == "oui":
    print("Ceci est un jeu ressemblant beaucoup  sauf que le jeu ne se deroule qu'en texte seulement."
          "\nVous aurez des rencontres aleatoire avec des enemis. Vous aurez le choix entre 3 classes qui ont chacun des"
          "\ndes capacites differentes. Appuyez sur entrer pour continuer.")
    input()
elif regle == "non":
    print("Tres bien, appuyez sur entrer pour continuer")
    input()

print("Veuillez entrer votre pseudo: ")
player = Player(input())
pyromane = Classes("pyromane", 5, 35, "arme en rapport avec le feu")
sorcier  = Classes("sorcier", 3, 45, "arme en rapport avec la magie")
chevalier = Classes("chevalier", 8, 30, "Les épées")
z = True
while z:
    print("Vous avez le choix entre \n 1.Le pyromane\n2.Le Sorcier\n3.Le chevalier\n(veuillez choisir en ecrivant le numero)")
    choix_classes = input()
    if choix_classes == "1":
        print("Le", pyromane.name,"a", pyromane.attack, "d'attaque,", pyromane.vie, "de vie et a acces aux",
              pyromane.possibilite_arme, "Etes-vous sur de vouloir garder cette classe? (oui/non)")
    elif choix_classes == "2":
        print("Le", sorcier.name,"a", sorcier.attack, "d'attaque,", sorcier.vie, "de vie et a acces aux",
              sorcier.possibilite_arme, "Etes-vous sur de vouloir garder cette classe? (oui/non)")
    elif choix_classes == "2":
        print("Le", chevalier.name,"a", chevalier.attack, "d'attaque,", chevalier.vie, "de vie et a acces aux",
              chevalier.possibilite_arme, "Etes-vous sur de vouloir garder cette classe? (oui/non)")
    choix_classes2 = input()
    if choix_classes2 == "oui":
        z = False
    elif choix_classes2 == "non":
        z = True
print("tg g pas encore coder le reste")
input()