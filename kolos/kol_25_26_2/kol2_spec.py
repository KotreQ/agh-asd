# kol1_spec.py

ALLOWED_TIME = 2


# format testów
# TESTS = [ {"arg":arg0, "hint": hint0}, {"arg":arg1, "hint": hint1}, ... ]

TEST_SPEC = [
    (-1, -1, -1, 1),
    (8, 12, 3, 0),
    (50, 52, 1, 19),
    (100, 103, 4, 15),
    (300, 307, 1, 75),
    (5000, 5001, 1, 753),
    (6000, 6002, 3, 1437),
    (7000, 7005, 8, 99),
    (8000, 8010, 15, 206),
    (9000, 9050, 20, 85),
    (50000, 50001, 20, 1459),
    (60000, 60002, 15, 2137),
    (70000, 70005, 8, 1879),
    (80000, 80010, 3, 9870),
    (90000, 90050, 1, 3303),
    (50000, 50001, 5000, 6),
    (60000, 60002, 6000, 1),
    (70000, 70005, 7000, 4),
    (80000, 80010, 8000, 22),
    (90000, 90050, 9000, 0)
]


def gentest(n, m, k, hint):
    if n == -1:
        mosty = [
            (1, 3, 'F'), (3, 4, 'F'), (2, 4, 'B'),
            (2, 5, 'B'), (4, 6, 'B'), (6, 7, 'F')
        ]
        poczty = [5, 7]
        sp = 1
        return [mosty, poczty, sp], hint

    from testy import MY_random

    M = set([(i, i + 1, MY_random() % 2) for i in range(1, n)])
    while len(M) < m:
        a = MY_random() % n + 1
        b = MY_random() % n + 1
        if a > b:
            a, b = b, a
        c = MY_random() % 2
        M.add((a, b, c))
    M = list(M)

    P = [0 for _ in range(n)]
    while sum(P) < k:
        idx = MY_random() % n
        P[idx] = 1

    s = 1

    permutation = list(range(1, n + 1))
    for _ in range(3 * n):
        i = MY_random() % n
        j = MY_random() % n
        permutation[i], permutation[j] = permutation[j], permutation[i]

    mosty = []
    for u, v, col in M:
        mosty.append((permutation[u - 1], permutation[v - 1], 'F' if col == 0 else 'B'))

    poczty = []
    for i, p in enumerate(P):
        if p == 1:
            poczty.append(permutation[i])

    sp = permutation[s - 1]

    return [mosty, poczty, sp], hint
