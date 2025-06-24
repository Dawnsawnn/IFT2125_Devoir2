# Nom, Matricule
# Nom, Matricule

import sys
sys.setrecursionlimit(10**7)

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

def placerFrites(n, points, k):

    N = n
    size = 2 * N
    g = [[] for _ in range(size)]
    def add(u, v):
        g[u].append(v)

    # Conflits même ligne
    rows = {}
    for i, (x, y) in enumerate(points):
        rows.setdefault(y, []).append((x, i))
    for lst in rows.values():
        lst.sort()
        xs, idxs = zip(*lst)
        l = 0
        for r in range(len(xs)):
            while xs[r] - xs[l] > 2 * k:
                l += 1
            for m in range(l, r):
                i, j = idxs[m], idxs[r]
                add(i, j + N)
                add(j, i + N)

    # Conflits même colonne
    cols = {}
    for i, (x, y) in enumerate(points):
        cols.setdefault(x, []).append((y, i))
    for lst in cols.values():
        lst.sort()
        ys, idxs = zip(*lst)
        l = 0
        for r in range(len(ys)):
            while ys[r] - ys[l] > 2 * k:
                l += 1
            for m in range(l, r):
                i, j = idxs[m], idxs[r]

                add(i + N, j)
                add(j + N, i)

    visited = [False] * size
    order = []
    def dfs1(u):
        visited[u] = True
        for v in g[u]:
            if not visited[v]:
                dfs1(v)
        order.append(u)

    for u in range(size):
        if not visited[u]:
            dfs1(u)

    # graphe inverse
    gr = [[] for _ in range(size)]
    for u in range(size):
        for v in g[u]:
            gr[v].append(u)

    comp = [-1] * size
    cid = 0
    def dfs2(u):
        comp[u] = cid
        for v in gr[u]:
            if comp[v] < 0:
                dfs2(v)

    for u in reversed(order):
        if comp[u] < 0:
            dfs2(u)
            cid += 1

    for i in range(N):
        if comp[i] == comp[i + N]:
            return False
    return True


   

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
