from egz3atesty import runtests


def snow( T, I ):
    # tu prosze wpisac wlasna implementacje

    n = len(I)

    A = []
    B = []
    for a, b in I:
        A.append(a)
        B.append(b)
    A.sort()
    B.sort()

    j = 0
    val = 0
    result = 0

    for i in range(n):
        val += 1

        start = A[i]
        while B[j] < start:
            val -= 1
            j += 1

        if val > result:
            result = val

    return result

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( snow, all_tests = True )
