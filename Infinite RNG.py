import random


def get_title():
    # Créer une liste pondérée avec les titres et leurs chances associées
    titles_with_chances = [
        ("Normal", 50),
        ("Uncommon", 25),
        ("Rare", 12),
        ("Epic", 7),
        ("Legendary", 5),
        ("Mythique", 1)
    ]

    # Créer la liste pondérée en fonction des chances
    titles = []
    for title, chance in titles_with_chances:
        titles.extend([title] * chance)

    # Choisir un titre au hasard
    selected_title = random.choice(titles)
    #result = ""
    # Trouver les chances associées au titre sélectionné
    for title, chance in titles_with_chances:
        if title == selected_title:
            print(f"Vous avez obtenu : {selected_title} ({chance}/100 chances)")
            # result = f"Vous avez obtenu : {selected_title} ({chance}/100 chances)"
            break

    #return result

def get_des():
    nb_des_with_chances = [
        ("1 dé", 15),
        ("3 dés", 40),
        ("5 dés", 15),
        ("10 dés", 10),
        ("25 dés", 10),
        ("50 dés", 7),
        ("100 dés", 3)
    ]

    # Créer la liste pondérée en fonction des chances
    des = []
    for title, chance in nb_des_with_chances:
        des.extend([title] * chance)

    selected_des = random.choice(des)

    print("------------Marchant---------------")
    print("Vous avez gagné",selected_des,"!")



# Test du système
for i in range(10):
    get_title()
print()
print("Voulez vous voir le marchant ?")
rep = input()
if rep == "oui" :
    get_des()
print("Merci d'avoir joué ! 😊, Si vous avez des idées pour améliorer le RNG, n'hésitez pas à me demander !")
