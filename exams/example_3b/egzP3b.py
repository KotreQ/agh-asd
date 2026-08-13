from egzP3btesty import runtests 
from queue import PriorityQueue


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


def lufthansa ( G ):
    #tutaj proszę wpisać własną implementację

    E = []
    n = len(G)

    for u, l in enumerate(G):
        for v, w in l:
            if v < u:
                continue

            E.append((w, u, v))

    E.sort(reverse=True)

    uf = UnionFind(n)
    additional_count = 0
    result = 0
    for w, u, v in E:
        if uf.find(u) == uf.find(v):
            additional_count += 1
            if additional_count > 1:
                result += w
        else:
            uf.union(u, v)

    return result

runtests ( lufthansa, all_tests=True )