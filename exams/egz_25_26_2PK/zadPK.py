# Bartłomiej Kochanek 430260
#
# Opis algorytmu:
# Z treści zadania wynika że musimy podzielić graf na jakimś z jego mostów. Znajdujemy wszystkie mosty w grafie używając algorytmu Tarjana. Dla każdego mostu, sprawdzamy jaki będzie wynik algorytmu poprzez zliczenie ile wierzchołków mamy w każdej z oddzielonych części. Jeśli jest to najlepszy wynik jak narazie to go zapisujemy.
#
# Złożoność obliczeniowa: O(VE)
# Złożoność pamięciowa: O(V+E)


from zadPKtesty import runtests


def get_bridges(G):  # O(V+E)
    n = len(G)
    visited = [False for _ in range(n)]
    disc = [-1 for _ in range(n)]
    low = [-1 for _ in range(n)]
    parent = [-1 for _ in range(n)]

    bridges = []
    dfs_time = 0

    def dfs(u):
        nonlocal dfs_time
        visited[u] = True
        disc[u] = low[u] = dfs_time
        dfs_time += 1

        children = 0

        for v in G[u]:
            if not visited[v]:
                parent[v] = u
                children += 1

                dfs(v)

                low[u] = min(low[u], low[v])

                if low[v] > disc[u]:
                    bridges.append((u, v))

            elif v != parent[u]:
                low[u] = min(low[u], disc[v])

    dfs(0)

    return bridges


class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parent = [i for i in range(self.n)]
        self.rank = [0 for _ in range(self.n)]

    def find(self, a) -> int:
        if self.parent[a] != a:
            self.parent[a] = self.find(self.parent[a])

        return self.parent[a]

    def union(self, a, b) -> bool:
        a = self.find(a)
        b = self.find(b)

        if a == b:
            return False

        if self.rank[a] < self.rank[b]:
            self.parent[a] = b
        else:
            self.parent[b] = a
            if self.rank[a] == self.rank[b]:
                self.rank[a] += 1

        return True

    def get_counts(self) -> dict[int, int]:
        counts = {}
        for v in range(self.n):
            v = self.find(v)
            if v not in counts:
                counts[v] = 0
            counts[v] += 1

        return counts


def partition(G):
    # tu prosze wpisac wlasna implementacje

    n = 0
    for u, v in G:
        n = max(n, u+1)
        n = max(n, v+1)

    GG = [[] for _ in range(n)]
    for u, v in G:
        GG[u].append(v)
        GG[v].append(u)

    bridges = [(min(u, v), max(u, v)) for u, v in get_bridges(GG)]

    if len(bridges) == 0:
        return -1

    best_result = float("inf")

    for cur_bridge in bridges:
        uf = UnionFind(n)

        for u, v in G:
            if u > v:
                u, v = v, u

            if (u, v) == cur_bridge:
                continue

            uf.union(u, v)

        union_counts = uf.get_counts()
        a_count, b_count = union_counts.values()

        result = abs(a_count - b_count)
        if result < best_result:
            best_result = result

    return best_result


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( partition, all_tests = True)
