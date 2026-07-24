from egz1Btesty import runtests
from math import inf as INF


# Czy istnieje ścieżka z s do t, wyłączając krawędź (s,t)
def dfs_find(G, s, t):
    n = len(G)
    visited = [False for _ in range(n)]

    def dfs(v):
        if visited[v]:
            return
        visited[v] = True

        if v == t:
            return True
        
        for u in G[v]:
            if v == s and u == t:
                continue

            if dfs(u):
                return True
        
        return False

    return dfs(s)


def critical(V, E):
    G = [[] for _ in range(V)]

    for v, u in E:
        G[v].append(u)

    counter = 0

    for v, u in E:
        if not dfs_find(G, v, u):
            counter += 1

    return counter


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(critical, all_tests = True)

    
