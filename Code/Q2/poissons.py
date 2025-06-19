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


def main(args):
    """Fonction main"""
    input_file = args[0]
    output_file = args[1]
    fish = read(input_file)

    pairs = 0

    # Solution naïve
    for i in range(len(fish)):
        F = fish[i]
        for f in fish[i+1:]:
            if f < F/2: pairs += 1

    write(str(pairs), output_file)


# NE PAS TOUCHER
if __name__ == "__main__":
    main(sys.argv[1:])
