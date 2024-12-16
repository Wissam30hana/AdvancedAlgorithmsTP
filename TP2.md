import time
import random

# Fonction pour mesurer le temps d'exécution
def mesurer_temps(fonction, *args):
    debut = time.perf_counter()
    resultat = fonction(*args)
    fin = time.perf_counter()
    return resultat, fin - debut

# 1. Tri par sélection
def tri_selection(tableau):
    comparaisons, mouvements = 0, 0
    n = len(tableau)
    for i in range(n):
        min_indice = i
        for j in range(i + 1, n):
            comparaisons += 1
            if tableau[j] < tableau[min_indice]:
                min_indice = j
        if min_indice != i:
            tableau[i], tableau[min_indice] = tableau[min_indice], tableau[i]
            mouvements += 1
    return tableau, comparaisons, mouvements

# 2. Tri à bulles
def tri_bulles(tableau):
    comparaisons, mouvements = 0, 0
    n = len(tableau)
    for i in range(n):
        for j in range(0, n - i - 1):
            comparaisons += 1
            if tableau[j] > tableau[j + 1]:
                tableau[j], tableau[j + 1] = tableau[j + 1], tableau[j]
                mouvements += 1
    return tableau, comparaisons, mouvements

# 3. Tri par insertion (par échanges)
def tri_insertion_echanges(tableau):
    comparaisons, mouvements = 0, 0
    n = len(tableau)
    for i in range(1, n):
        j = i
        while j > 0 and tableau[j] < tableau[j - 1]:
            comparaisons += 1
            tableau[j], tableau[j - 1] = tableau[j - 1], tableau[j]
            mouvements += 1
            j -= 1
        if j > 0:
            comparaisons += 1
    return tableau, comparaisons, mouvements

# 4. Tri par insertion (par décalages)
def tri_insertion_decalages(tableau):
    comparaisons, mouvements = 0, 0
    n = len(tableau)
    for i in range(1, n):
        valeur_courante = tableau[i]
        j = i - 1
        while j >= 0 and tableau[j] > valeur_courante:
            comparaisons += 1
            tableau[j + 1] = tableau[j]
            mouvements += 1
            j -= 1
        tableau[j + 1] = valeur_courante
        mouvements += 1
        if j >= 0:
            comparaisons += 1
    return tableau, comparaisons, mouvements

# Générer un tableau
def generer_tableau(taille, ordre="aleatoire"):
    if ordre == "aleatoire":
        return [random.randint(1, taille * 10) for _ in range(taille)]
    elif ordre == "ascendant":
        return list(range(1, taille + 1))
    elif ordre == "descendant":
        return list(range(taille, 0, -1))

# Exécuter les tests
def executer_tests():
    tailles = [1000, 10000, 100000]
    ordres = ["aleatoire", "ascendant", "descendant"]
    algorithmes = {
        "Tri par sélection": tri_selection,
        "Tri à bulles": tri_bulles,
        "Tri par insertion (échanges)": tri_insertion_echanges,
        "Tri par insertion (décalages)": tri_insertion_decalages
    }
    
    for taille in tailles:
        for ordre in ordres:
            tableau_original = generer_tableau(taille, ordre)
            print(f"\nTaille: {taille}, Ordre: {ordre}")
            
            for nom_algo, algo in algorithmes.items():
                tableau = tableau_original[:]
                _, temps_execution = mesurer_temps(algo, tableau)
                tableau_trie, comparaisons, mouvements = algo(tableau)
                print(f"{nom_algo}: Comparaisons={comparaisons}, Mouvements={mouvements}, Temps={temps_execution:.4f} secondes")

# Lancer les tests git status
if __name__ == "__main__":
    executer_tests()
