from egz1atesty import runtests

from queue import PriorityQueue


def distances(G, start):
    n = len(G)
    distance = [float("inf") for _ in range(n)]

    visited = [False for _ in range(n)]
    q = PriorityQueue()  # structure: (full_cost, target_idx)

    q.put((0, start))

    while q.qsize() > 0:
        full_cost, v = q.get()

        if visited[v]:
            continue
        visited[v] = True
        distance[v] = full_cost

        for u, cost in G[v]:
            q.put((full_cost + cost, u))
    
    return distance


def armstrong(B, G, s, t):
    n = 0
    
    for a, b, _ in G:
        if a >= n:
            n = a+1
        if b >= n:
            n = b+1
    
    neighbours = [[] for _ in range(n)]
    for a, b, c in G:
        neighbours[a].append((b, c))
        neighbours[b].append((a, c))
    
    bikes = [(1, 1) for _ in range(n)]
    for idx, a, b in B:
        is_better = (a * bikes[idx][1]) < (bikes[idx][0] * b)
        if is_better:
            bikes[idx] = (a, b)
    
    start_distances = distances(neighbours, s)
    finish_distances = distances(neighbours, t)
    
    current_best = float("inf")

    for v in range(n):
        full_time = start_distances[v] + finish_distances[v] * bikes[v][0] // bikes[v][1]
        if full_time < current_best:
            current_best = full_time

    return current_best


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( armstrong, all_tests = True )
