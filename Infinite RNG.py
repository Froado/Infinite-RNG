import random


def get_title():
    # Créer une liste pondérée avec les titres et leurs chances associées
    titles_with_chances = [
        ("Normal", 50),
        ("Uncommon", 25),
        ("Rare", 12),
        ("Epic", 6),
        ("Legendary", 6)
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


# Test du système
for i in range(10):
    get_title()
print()
print("Merci d'avoir joué ! 😊, Si vous avez des idées pour améliorer le RNG, n'hésitez pas à me demander !")
