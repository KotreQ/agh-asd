from egz2btesty import runtests

from collections import deque


def tory_amos( E, A, B ):
    n = 0
    for v, u, _, _ in E:
        if v >= n:
            n = v + 1
        if u >= n:
            n = u + 1

    G = [[] for _ in range(n)]

    for v, u, dist, type_ in E:
        type_ = 0 if type_ == "I" else 1
        G[v].append((u, dist, type_))
        G[u].append((v, dist, type_))
    
    # structure in queue: (vertex, equipped_wheels) - add transition weight when leaving station

    visited = [[False, False] for _ in range(n)]
    
    visited[A][0] = True
    visited[A][1] = True
    QUEUE_COUNT = 31

    cur_weight = 0
    queues = [deque() for _ in range(QUEUE_COUNT)]

    for v, d, t in G[A]:
        queues[d].append((v, t))
    
    while True:
        while len(queues[cur_weight % QUEUE_COUNT]) == 0:
            cur_weight += 1
        
        while len(queues[cur_weight % QUEUE_COUNT]) > 0:
            v, wheels = queues[cur_weight % QUEUE_COUNT].popleft()
            if visited[v][wheels]:
                continue
            visited[v][wheels] = True

            if v == B:
                return cur_weight
            
            for u, d, t in G[v]:
                if wheels == t:
                    cost = 5 if t == 0 else 10
                else:
                    cost = 20
                cost += d

                target_queue = (cur_weight + cost) % QUEUE_COUNT
                queues[target_queue].append((u, t))


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( tory_amos, all_tests = True )
