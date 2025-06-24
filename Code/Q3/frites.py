# Nom, Matricule
# Nom, Matricule

import sys

def read(input_file):
    file = open(input_file, "r")
    lines = file.readlines()
    file.close()
    n = int(lines[0])
    points = [tuple(map(int, line.split())) for line in lines[1:n+1]]
    return n, points

def write(str_content, output_file):
    file = open(output_file, "w")
    file.write(str_content)
    file.close()

"""def placerFrites(n, pts, k):
    orientation = [0] * n
    
    while True:
        ok = True
        for a in range(n):
            x, y = pts[a]
            r = orientation[a]
            for b in range(a):
                x2, y2 = pts[b]
                r2 = orientation[b]
                # conflit H–H sur même ligne
                if r == r2 == 0 and y == y2 and abs(x - x2) <= 2*k:
                    ok = False
                    break
                # conflit V–V sur même colonne
                if r == r2 == 1 and x == x2 and abs(y - y2) <= 2*k:
                    ok = False
                    break
            if not ok:
                break
        if ok:
            return True

"""


    

def max_k(n, points):
    # Infini?
    if placerFrites(n, points, 10**9):
        return "infini"
    # Recherche binaire
    left, right, best = 0, 10**9, 0
    while left <= right:
        mid = (left + right) // 2
        if placerFrites(n, points, mid):
            best = mid
            left = mid + 1
        else:
            right = mid - 1
    return str(best) if best > 0 else "0"

def main(args):
    input_file, output_file = args
    n, points = read(input_file)
    res = max_k(n, points)
    write(res, output_file)

# NE PAS TOUCHER
if __name__ == "__main__":
    main(sys.argv[1:])
