# Bartłomiej Kochanek 430260
# 
# Złożoność obliczeniowa:

from kol1_test import runtests
from random import randint


def partition(A, p, q): # [p,q]
    pivot_idx = randint(p, q)
    pivot = A[pivot_idx]

    A[q], A[pivot_idx] = A[pivot_idx], A[q]

    i = p
    j = q - 1

    while i <= j:
        if A[i] > pivot and A[j] < pivot:
            A[i], A[j] = A[j], A[i]

        if A[i] <= pivot:
            i += 1

        if A[j] >= pivot:
            j -= 1

    A[q], A[i] = A[i], A[q]

    return i

def qsort(A, p, r):
    if p >= r:
        return
    
    q = partition(A, p, r)
    qsort(A, p, q-1)
    qsort(A, q+1, r)


def count_lower(A, x) -> int:  # ile elementów jest mniejszych od podanej wartości
    n = len(A)

    result = 0

    col = n
    for row in range(n):
        while col > 0 and A[row] * A[col-1] >= x:
            col -= 1

        result += col

    return result



def k_big(A, k):
    # tu prosze wpisac wlasna implementacje

    n = len(A)
    qsort(A, 0, n-1)
    target_idx = n**2 - k

    l = 0
    r = n**2 - 1

    while l < r:
        p = (l+r)//2

        lower = count_lower(A, p)

        if lower <= target_idx:
            l = p+1
        elif lower > target_idx:
            r = p

    return l-1


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(k_big, all_tests = True)