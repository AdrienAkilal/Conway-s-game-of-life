#                            Regles du jeu
# Une cellule vivante avec moins de 2 voisins vivants meurt (solitude).
# Une cellule vivante avec 2 ou 3 voisins vivants survit.
# Une cellule vivante avec plus de 3 voisins vivants meurt (surpopulation).
# Une cellule morte avec exactement 3 voisins vivants devient vivante (reproduction).


def afficher_grille(grille):
    for ligne in grille:
        print(" ".join(['#' if cellule else '.' for cellule in ligne]))
    print()

# fonction demandant à l'utilisateur une grille avec des cellules vivantes
def initialiser_grille():
    rows = int(input("Entrez le nombre de lignes de la grille : "))
    cols = int(input("Entrez le nombre de colonnes de la grille : "))
    grille = [[0 for _ in range(cols)] for _ in range(rows)]

    print("Entrez les coordonnées des cellules vivantes (format : ligne colonne). Tapez 'fin' pour terminer :")
    while True:
        entree = input("Cellule vivante : ").strip()
        if entree.lower() == 'fin':
            break
        try:
            x, y = map(int, entree.split())
            if 0 <= x < rows and 0 <= y < cols:
                grille[x][y] = 1
            else:
                print("Coordonnées hors de la grille, réessayez.")
        except ValueError:
            print("Entrée invalide. Veuillez entrer deux nombres séparés par un espace.")
    return grille

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
                # Règles pour une cellule vivante
                nouvelle_grille[x][y] = 1 if 2 <= voisins <= 3 else 0
            else:
                # Règle pour une cellule morte
                nouvelle_grille[x][y] = 1 if voisins == 3 else 0
    return nouvelle_grille

# boucle du jeu
grille = initialiser_grille()
print("État initial :")
afficher_grille(grille)

for _ in range(5):  
    grille = mettre_a_jour(grille)
    afficher_grille(grille)
