# Jérémie Dupuis, 20276905
# Samuel Michaud, 20244446

import sys

def read(input_file):
    """Fonction pour lire un fichier."""
    file = open(input_file, "r")
    lines = file.readlines()
    file.close()

    n = int(lines[0])

    fish = list(map(lambda n: int(n), lines[1].split(" ")))

    if len(fish) != n: raise ValueError(f"Le nombre de poissons ne correspond pas à {n}.")

    return fish


def write(str_content, output_file):
    """Fonction pour écrire dans un fichier."""
    file = open(output_file, "w")
    file.write(str_content)
    file.close()


def count_pairs(fish):

    def sort_count(fish):
        if len(fish) <= 1:
            return 0, fish
        mid = len(fish) // 2
        counter_left, left = sort_count(fish[:mid])
        counter_right, right = sort_count(fish[mid:])
        counter_both, merged = merge_count(left, right)
        return counter_left + counter_right + counter_both, merged

    def merge_count(left, right):
        counter = 0
        j = 0
        for i in range(len(left)):
            while j < len(right) and left[i] > 2 * right[j]:
                j += 1
            counter += j
        merged = []
        i = 0
        j = 0
        while

def main(args):
    """Fonction main"""
    input_file = args[0]
    output_file = args[1]
    fish = read(input_file)

    pairs = count_pairs(fish)


    write(str(pairs), output_file)


# NE PAS TOUCHER
if __name__ == "__main__":
    main(sys.argv[1:])
