from egz2btesty import runtests


def magic( C ):
    # tu prosze wpisac wlasna implementacje
    # nie lol

    n = len(C)
    F = [-1 for _ in range(n)]
    # F[i] = ile możemy mieć maksymalnie złota wchodząc do komnaty i
    F[0] = 0

    for i in range(n):
        if F[i] == -1:  # nie da się dojść do komnaty
            continue

        g = C[i][0]
        rooms = C[i][1:4]

        for k, w in rooms:
            if w == -1:  # drzwi zablokowane
                continue

            diff = g - k
            if diff > 10 or F[i] + diff < 0:  # musimy wziąć za dużo albo nas nie stać
                continue

            new_gold = F[i] + diff
            F[w] = max(F[w], new_gold)

    return F[n-1]

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( magic, all_tests = True )
