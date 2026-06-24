# Bartłomiej Kochanek 430260
#
# Opis algorytmu:
# Każdy z wierzchołków rozmnażamy na dwa: taki, na którym zostawiamy ubraną taką czapkę jaką mamy, i drugi, na którym zmieniamy ubraną czapkę
# Korzystamy z algorytmu bfs, który w przypadku zmiany czapki dodaje wierzchołek z powrotem na sam koniec kolejki, żeby wierzchołki które wymagają więcej zmian były przetwarzane później
# Przetwarzając każdy wierzchołek dodajemy 1 do licznika jeśli dokonaliśmy zmiany przez co dostajemy wynik kiedy dotrzemy już do poczty
#
# Złożoność obliczeniowa: O(m)


from kol2_test import runtests

from collections import deque


def to_adj_list(edges):
    max_v = -1

    for u, v, _ in edges:
        max_v = max(max_v, u)
        max_v = max(max_v, v)
    
    G = [[] for _ in range(max_v+1)]

    for u, v, g in edges:
        g = int_hat(g)
        G[u].append((v, g))
        G[v].append((u, g))
    
    return G


def int_hat(hat):
    if hat == 'F':
        return 0
    elif hat == 'B':
        return 1
    raise ValueError("Niepoprawna wartość czapki")


def change(mosty, poczty, s):
    G = to_adj_list(mosty)
    n = len(G)
    visited = [[False, False] for _ in range(n)]

    poczty = set(poczty)

    queue = deque()  # struktura w kolejce: (czy_wymaga_zmiany, liczba_zmian, wierzchołek, czapka)

    queue.append((False, 0, s, 0))
    queue.append((False, 0, s, 1))

    while len(queue) > 0:
        needs_change, change_count, v, hat = queue.popleft()

        if needs_change:
            new_hat = 0 if hat == 1 else 1
            queue.append((False, change_count + 1, v, new_hat))
            continue

        if visited[v][hat]:
            continue
        visited[v][hat] = True

        if v in poczty:
            return change_count

        for neigh, hat_req in G[v]:
            if hat != hat_req: # jeśli nie mamy odpowiedniej czapki, ignorujemy
                continue

            # nie zmieniamy czapki na kolejnym wierzchołku
            queue.append((False, change_count, neigh, hat))

            # zmieniamy czapkę na kolejnym wierzchołku
            queue.append((True, change_count, neigh, hat))


result = change(
    [
        (1, 2, "F"),
        (2, 3, "F"),
        (3, 4, "F"),
        (4, 5, "F"),
        (1, 6, "B"),
        (6, 5, "F")
    ],
    [5],
    1
)
print(result)

runtests(change, all_tests = True)
