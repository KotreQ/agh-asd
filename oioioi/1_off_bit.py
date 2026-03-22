import sys
from random import randint, seed


OIOIOI = False


def left(i):
    return 2*i+1

def right(i):
    return 2*i+2

def parent(i):
    return (i-1)//2


def heapify(A, i, n):
    max_idx = i
    l = left(i)
    r = right(i)

    if l < n and A[l] > A[max_idx]:
        max_idx = l
    if r < n and A[r] > A[max_idx]:
        max_idx = r

    if max_idx != i:
        A[i], A[max_idx] = A[max_idx], A[i]
        heapify(A, max_idx, n)

def heap_sort(A):
    N = len(A)
    for i in range(parent(N-1), -1, -1):
        heapify(A, i, N)
    
    for n in range(N-1, 0, -1):
        A[n], A[0] = A[0], A[n]
        heapify(A, 0, n)


def update_BIT(bit, idx, val):
    n = len(bit) - 1
    while idx <= n:
        bit[idx] += val
        idx += idx & -idx

def prefix_BIT(bit, idx):
    res = 0
    while idx > 0:
        res += bit[idx]
        idx -= idx & -idx
    return res


def solution(T):
    n = len(T)

    uniq = list(set(T))

    heap_sort(uniq)
    ranks = {word: idx+1 for idx, word in enumerate(uniq)}

    # Binary Indexed Tree
    bit = [0] * (len(uniq) + 1) # Indexed from 1, number of occurrences of a specific rank

    max_dom = 0

    for word in T:
        rank = ranks[word]
        dom = prefix_BIT(bit, rank-1)
        update_BIT(bit, rank, 1)

        if dom > max_dom:
            max_dom = dom

    return max_dom


if __name__ == "__main__":
    def generate_random_string(length):
        return ''.join(chr(randint(97, 122)) for _ in range(length))
    
    if OIOIOI:
        n = int(sys.stdin.readline().strip())
        words = [sys.stdin.readline().strip() for _ in range(n)]
        print(solution(words))
    else:
        seed(1)
        test_def = [
            (10, 5, 10, 6),
            (100, 5, 10, 88),
            (100, 20, 100, 91),
            (10000, 10, 30, 9901)
        ]
        ok = 0
        for idx, (n, m_low, m_high, ans) in enumerate(test_def):
            print("Test", idx + 1)
            words = [generate_random_string(randint(m_low, m_high)) for _ in range(n)]
            result = solution(words)
            if result == ans:
                print("OK")
                ok += 1
            else:
                print("Błąd!")
        print("Wynik:", ok, "/", len(test_def))
