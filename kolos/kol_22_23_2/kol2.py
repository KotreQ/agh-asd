from kol2testy import runtests


class UnionFind:
    def __init__(self, N):
        self.N = N
        self.parent = [n for n in range(N)]
        self.rank = [0 for _ in range(N)]

    def find(self, a):
        if self.parent[a] != a:
            self.parent[a] = self.find(self.parent[a])
        
        return self.parent[a]

    def union(self, a, b):
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
    

def beautree(G):
    n = len(G)

    edges = []

    for v in range(n):
        for u, w in G[v]:
            if v > u:
                continue

            edges.append((w, v, u))

    m = len(edges)

    edges.sort()

    correct_weights = []
    
    # length of range = n-1
    for start in range(m - n + 2):
        end = start + n - 1

        counter = 0
        correct = True

        uf = UnionFind(n)

        for e_idx in range(start, end):
            w, v, u = edges[e_idx]

            if not uf.union(v, u):
                correct = False
                break

            counter += w
        
        if correct:
            correct_weights.append(counter)
    
    if len(correct_weights) == 0:
        return None
    return min(correct_weights)


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( beautree, all_tests = True )
