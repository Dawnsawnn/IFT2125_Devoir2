# Jérémie Dupuis, 20276905
# Samuel Michaud, 20244446

import sys

def read(input_file):

    file = open(input_file, "r")
    lines = file.readlines()
    file.close()

    n = int(lines[0])

    fish = list(map(lambda n: int(n), lines[1].split(" ")))

    if len(fish) != n: raise ValueError(f"Le nombre de poissons ne correspond pas à {n}.")

    return fish


def write(str_content, output_file):

    file = open(output_file, "w")
    file.write(str_content)
    file.close()

# Implémentation de Merge Sort modifiée pour compter le nombre de paires de poissons.
# Basée sur https://www.w3schools.com/dsa/dsa_algo_mergesort.php
def count_pairs(fish):

    # Si la liste a 0 ou 1 élément, il n'y a pas de paires 
    if len(fish) <= 1:
        return 0

    # Divise la liste en deux moitiés
    mid = len(fish) // 2
    left = fish[:mid]
    right = fish[mid:]

    # Appels récursifs sur chaque moitié
    counter_left = count_pairs(left)
    counter_right = count_pairs(right)
    # Compte les paires entre les deux moitiés
    counter_both = 0

    j = 0
    # Compte les paires entre les deux moitiés
    for i in range(len(left)):

        while j < len(right) and left[i] > 2 * right[j]:
            j += 1
        counter_both += j


    merged = []
    i = j = 0
    # Fusionne les deux sous-listes triées en une seule liste triée
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])
    fish[:] = merged
    
    # Retourne le nombre total de paires 
    return counter_left + counter_right + counter_both


def main(args):

    input_file = args[0]
    output_file = args[1]
    fish = read(input_file)

    pairs = count_pairs(fish)


    write(str(pairs), output_file)


# NE PAS TOUCHER
if __name__ == "__main__":
    main(sys.argv[1:])
