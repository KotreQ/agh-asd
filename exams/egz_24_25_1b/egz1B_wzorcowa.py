from egz1Btesty import runtests
from math import inf as INF


def critical(V, E):
    G = [[] for _ in range(V)]

    for v, u in E:
        G[v].append(u)

    result = 0

    for s in range(V):
        count = [0 for _ in range(V)]

        def dfs(v):
            count[v] += 1
            if count[v] > 1:
                return

            for u in G[v]:
                dfs(u)
        
        dfs(s)

        for v in G[s]:
            if count[v] == 1:
                result += 1
        
    return result


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(critical, all_tests = True)

    
