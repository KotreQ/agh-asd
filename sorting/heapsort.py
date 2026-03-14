import random


def btree_left(i):
    return 2 * i + 1


def btree_right(i):
    return 2 * i + 2


def btree_parent(i):
    return (i - 1) // 2


def heapify(A, n, i):
    max_i = i
    left = btree_left(i)
    right = btree_right(i)

    if left < n and A[left] > A[max_i]:
        max_i = left

    if right < n and A[right] > A[max_i]:
        max_i = right

    if max_i != i:
        A[i], A[max_i] = A[max_i], A[i]
        heapify(A, n, max_i)


def heap_sort(A):
    n = len(A)

    last_non_leaf = btree_parent(n - 1)
    for i in range(last_non_leaf, -1, -1):
        heapify(A, n, i)

    for i in range(n - 1, 0, -1):
        A[0], A[i] = A[i], A[0]
        heapify(A, i, 0)


def main() -> None:
    A = random.choices(range(100), k=20)
    print(A)

    heap_sort(A)
    print(A)

if __name__ == "__main__":
    main()
