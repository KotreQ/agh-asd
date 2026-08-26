# Bartłomiej Kochanek 430260
# Tworzymy całą tabliczkę mnożenia w tablicy jednowymiarowej i zwracamy k-tą największą z nich za pomogą quick select
# Złożoność obliczeniowa: n^2

from kol1_test import runtests
from random import randint


def partition(A, p, q):
    pivot_idx = randint(p, q)
    pivot = A[pivot_idx]

    A[q], A[pivot_idx] = A[pivot_idx], A[q]

    i = p
    j = q-1

    while i <= j:
        if A[i] > pivot and A[j] < pivot:
            A[i], A[j] = A[j], A[i]
        
        if A[i] <= pivot:
            i += 1
        
        if A[j] >= pivot:
            j -= 1
    
    A[q], A[i] = A[i], A[q]

    return i


def quick_sort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quick_sort(A, p, q-1)
        quick_sort(A, q+1, r)


def quick_select(A, p, q, k):
    while True:
        i = partition(A, p, q)

        if i == k:
            return A[i]
        
        elif i < k:
            p = i + 1
        
        elif i > k:
            q = i - 1


def Sn(a1, r, n):  # suma ciągu arytmetycznego
    return n * a1 + (r * n*(n-1) // 2)



def k_big(A, k):
    # tu prosze wpisac wlasna implementacje

    n = len(A)

    T = []
    for i in range(n):
        for j in range(n):
            T.append(A[i] * A[j])

    target_idx = n**2 - k

    return quick_select(T, 0, n**2-1, target_idx)



# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(k_big, all_tests = True)