# Jérémie Dupuis, 20276905
# Samuel Michaud, 20244446

import sys
sys.setrecursionlimit(100000)
Inf = 10**10 # Stand-in pour infini, à ajuster selon l'input

def read(input_file):
    file = open(input_file, "r")
    lines = file.readlines()
    file.close()
    points = [tuple(map(int, line.split())) for line in lines[1:]]
    n = int(lines[0])
    if len(points) != n: raise ValueError(f"Le nombre de points ne correspond pas à {n}.")
    return n, points


def write(str_content, output_file):
    file = open(output_file, "w")
    file.write(str_content)
    file.close()


# n = taille de `points`
# points = liste de tuples (x ,y)
# k = demi-longueur des frites
def placerFrites(n, points, k):
    size = 2 * n
    g = [[] for _ in range(size)] # tableau de 2n tableaux vides
    def add(u, v): # add to i of g
        g[u].append(v)

    # Conflits même ligne
    rows = {} # dictionnaire des y: { y: [(x, index du point), chaque point sur ce y],
    for i, (x, y) in enumerate(points):
        rows.setdefault(y, []).append((x, i))

    for row in rows.values():
        row.sort() # tri par x
        xs, ids = zip(*row) # xs = liste des x, ids = liste des i
        l = 0
        for r in range(len(xs)):
            while xs[r] - xs[l] > 2 * k:
                l += 1
            # l est alors l'élément problématique le plus loin de r (le "premier" élément problématique)
            ri = ids[r]
            for m in range(l, r): # m va prendre successivement l'index des points trop proche de r
                mi = ids[m]
                add(mi, ri + n) # m → r
                add(ri, mi + n) # r → m

    # Conflits même colonne
    cols = {}
    for i, (x, y) in enumerate(points):
        cols.setdefault(x, []).append((y, i))

    for col in cols.values():
        col.sort() # tri par y
        ys, ids = zip(*col) # ys = liste des y, ids = liste des i
        l = 0
        for r in range(len(ys)):
            while ys[r] - ys[l] > 2 * k:
                l += 1
            ri = ids[r]
            for m in range(l, r):
                mi = ids[m]
                add(mi + n, ri) # m → r
                add(ri + n, mi) # r → m

    visited = [False] * size
    order = [] # Ordre de visite

    # Première visite en depth-first
    def dfs1(u):
        visited[u] = True
        for v in g[u]:
            if visited[v]: continue
            dfs1(v)
        order.append(u)

    for u in range(size):
        if visited[u]: continue
        dfs1(u)

    # Graphe inverse
    gi = [[] for _ in range(size)]
    for u in range(size):
        for v in g[u]:
            gi[v].append(u)

    # Deuxième visite en depth-first (graphe inverse)
    comp = [-1] * size
    cid = 0
    def dfs2(u):
        comp[u] = cid
        for v in gi[u]:
            if comp[v] >= 0: continue
            dfs2(v)

    for u in reversed(order):
        if comp[u] >= 0: continue
        dfs2(u)
        cid += 1

    for i in range(n):
        if comp[i] == comp[i+n]: return False
    return True


def maxk(n, points):
    if placerFrites(n, points, Inf):
        return "infini"
    # Recherche dichotomique
    min = 0
    max = Inf
    best = 0
    while min <= max:
        mid = (min + max) // 2
        if placerFrites(n, points, mid):
            best = mid
            min = mid + 1
        else:
            max = mid - 1
    return str(best) if best > 0 else "0"


def main(args):
    input_file, output_file = args
    n, points = read(input_file)
    sol = maxk(n, points)
    write(sol, output_file)


# NE PAS TOUCHER
if __name__ == "__main__":
    main(sys.argv[1:])
