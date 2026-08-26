import random


def select_pivot(A, p, r):
    if r - p <= 3:
        return p

    a = p
    b = (p+r) // 2
    c = r

    if A[a] < A[b]:
        if A[b] < A[c]:
            return b
        elif A[c] < A[a]:
            return a
        else:
            return c
    else:
        if A[a] < A[c]:
            return a
        elif A[c] < A[b]:
            return b
        else:
            return c


def partition(A, p, r):
    pivot_idx = select_pivot(A, p, r)
    pivot = A[pivot_idx]

    # move pivot to end
    A[r], A[pivot_idx] = A[pivot_idx], A[r]

    i = p
    j = r - 1

    while i <= j:
        if A[i] > pivot and A[j] < pivot:
            A[i], A[j] = A[j], A[i]

        if A[i] <= pivot:
            i += 1

        if A[j] >= pivot:
            j -= 1

    # move pivot to correct index
    A[r], A[i] = A[i], A[r]

    return i


def qsort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        qsort(A, p, q-1)
        qsort(A, q+1, r)


def quick_sort(A):
    qsort(A, 0, len(A)-1)


def main():
    A = random.choices(range(100), k=40)
    print(A)

    quick_sort(A)
    print(A)

    if A == sorted(A):
        print("SUCCESS")
    else:
        print("FAILURE")


if __name__ == "__main__":
    main()
