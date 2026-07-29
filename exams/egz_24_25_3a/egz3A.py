from egz3Atesty import runtests

def count_inverses(A):
    A = list(A)
    n = len(A)

    inverses = 0

    B = [0 for _ in range(n)]

    def merge(p, q, r):
        nonlocal inverses

        i = p
        j = q

        k = p

        while i < q and j < r:
            if A[i] <= A[j]:
                B[k] = A[i]
                i += 1
            else:
                B[k] = A[j]
                inverses += j-k
                j += 1

            k += 1

        while i < q:
            B[k] = A[i]
            i += 1
            k += 1

        while j < r:
            B[k] = A[j]
            j += 1
            k += 1

    def msort(p, r):
        if p >= r-1:
            return

        q = (p+r) // 2
        msort(p, q)
        msort(q, r)

        merge(p, q, r)
        for i in range(p, r):
            A[i] = B[i]


    msort(0, n)

    return inverses


def treecut( H, k ):
    n = len(H)

    l = 0
    r = n

    while l < r:
        cur = (l+r+1)//2
        val = count_inverses(H[:cur])

        if val > k:
            r = cur - 1
        else:
            l = cur

    return l



# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( treecut, all_tests = True )
