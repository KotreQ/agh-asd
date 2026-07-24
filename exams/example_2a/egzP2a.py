from egzP2atesty import runtests 
import random


def partition(T, p, q):
    pivot_idx = random.randint(p, q)
    pivot = T[pivot_idx][1]

    T[pivot_idx], T[q] = T[q], T[pivot_idx]

    i = p
    j = q-1

    while i <= j:
        a = T[i][1]
        b = T[j][1]
        if a > pivot and b < pivot:
            T[i], T[j] = T[j], T[i]
        
        if a <= pivot:
            i += 1
        
        if b >= pivot:
            j -= 1
    
    T[i], T[q] = T[q], T[i]

    return i


def qselects(T, p, q, targets):
    if len(targets) == 0:
        return

    if p >= q:
        return

    print(f"[{p}, {q}] -> {targets}")

    r = partition(T, p, q)

    low_targets = []
    high_targets = []
    for target in targets:
        if target < r:
            low_targets.append(target)
        elif target > r:
            high_targets.append(target)
    
    qselects(T, p, r-1, low_targets)
    qselects(T, r+1, q, high_targets)


def zdjecie(T, m, k):
    # T = lista[(nr_albumu, wysokość)]
    # m = ilość rzędów
    # k = ilość osób w najniższym rzędzie

    n = len(T)

    if m < 2:
        return

    lengths = list(range(k, k+m))
    indices = [0 for _ in range(m)]

    for i in range(1, m):
        indices[i] = indices[i-1] + lengths[i-1]    

    T_sorted = T.copy()
    qselects(T_sorted, 0, n-1, indices[1:])

    rows = [[] for _ in range(m)]
    for i in range(m):
        rows[i] = T_sorted[indices[i] : indices[i] + lengths[i]]
    
    i = 0

    for j in range(k):
        for row in range(m-1, -1, -1):
            T[i] = rows[row][j]
            i += 1
    
    for j in range(k, k+m-1):
        for row in range(m-1, (j-k), -1):
            T[i] = rows[row][j]
            i += 1

    return None


runtests ( zdjecie, all_tests=True )