from egz3atesty import runtests
from collections import deque


def mykoryza( G,T,d ):
    # tu prosze wpisac wlasna implementacje

    n = len(G)
    result = 0

    owner = [-1 for _ in range(n)]

    q = deque()  # struktura w kolejce: (id_grzyba, wierzchołek)
    for i, v in enumerate(T):
        q.append((i, v))

    while len(q) > 0:
        mush, v = q.popleft()

        if owner[v] != -1:
            continue
        owner[v] = mush

        if mush == d:
            result += 1

        for u in G[v]:
            q.append((mush, u))

    return result


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( mykoryza, all_tests = True )
