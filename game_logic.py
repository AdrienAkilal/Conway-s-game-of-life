#                            Regles du jeu
# Une cellule vivante avec moins de 2 voisins vivants meurt (solitude).
# Une cellule vivante avec 2 ou 3 voisins vivants survit.
# Une cellule vivante avec plus de 3 voisins vivants meurt (surpopulation).
# Une cellule morte avec exactement 3 voisins vivants devient vivante (reproduction).


def afficher_grille(grille):
    for ligne in grille:
        print(" ".join(['#' if cellule else '.' for cellule in ligne]))
    print()

def initialiser_grille():
    return [
        [0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ]

def compter_voisins(grille, x, y):
    voisins = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),         (0, 1),
        (1, -1), (1, 0), (1, 1)
    ]
    compteur = 0
    for dx, dy in voisins:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(grille) and 0 <= ny < len(grille[0]):
            compteur += grille[nx][ny]
    return compteur

def mettre_a_jour(grille):
    nouvelle_grille = [[0 for _ in range(len(grille[0]))] for _ in range(len(grille))]
    for x in range(len(grille)):
        for y in range(len(grille[0])):
            voisins = compter_voisins(grille, x, y)
            if grille[x][y] == 1:
                # Règles pour  cellule vivante
                nouvelle_grille[x][y] = 1 if 2 <= voisins <= 3 else 0
            else:
                # Règle pour  cellule morte
                nouvelle_grille[x][y] = 1 if voisins == 3 else 0
    return nouvelle_grille

# boucle du jeu 
grille = initialiser_grille()
print("État initial :")
afficher_grille(grille)

for _ in range(5): 
    grille = mettre_a_jour(grille)
    afficher_grille(grille)
