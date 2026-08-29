from collections import deque

from egz3atesty import runtests

def goodknight( G, s, t ):
    # tu prosze wpisac wlasna implementacje
    
    n = len(G)

    GG = [[] for _ in range(n)]
    for i in range(n-1):
        for j in range(i+1, n):
            w = G[i][j]
            if w != -1:
                GG[i].append((j, w))
                GG[j].append((i, w))

    # wierzchołek: (v, energia)
    Q_COUNT = 9
    queues = [deque() for _ in range(Q_COUNT)]
    queues[0].append((s, 16))

    cur_weight = 0
    visited = [[False for _ in range(17)] for _ in range(n)]  # visited[v, energy] = wierzchołek v z energią energy

    while True:
        while len(queues[cur_weight % Q_COUNT]) == 0:
            cur_weight += 1

        while len(queues[cur_weight % Q_COUNT]) > 0:
            v, energy = queues[cur_weight % Q_COUNT].popleft()
            if visited[v][energy]:
                continue
            visited[v][energy] = True

            if v == t:
                return cur_weight

            for u, w in GG[v]:
                if energy >= w:
                    queues[(cur_weight + w) % Q_COUNT].append((u, energy-w))

            queues[(cur_weight + 8) % Q_COUNT].append((v, 16))


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( goodknight, all_tests = True )
