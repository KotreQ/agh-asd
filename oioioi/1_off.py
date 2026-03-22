import sys
from random import randint, seed


OIOIOI = True 


def find_dominations(T):
    n = len(T)

    idx = list(range(n))
    temp = [0 for _ in range(n)]
    
    dominations = [0 for _ in range(n)]

    def merge(p, q, r):
        i = p
        j = q
        k = p

        first_count = 0

        while i < q and j < r:
            if T[idx[i]] < T[idx[j]]:
                temp[k] = idx[i]
                first_count += 1
                i += 1
            else:
                temp[k] = idx[j]
                dominations[idx[j]] += first_count
                j += 1
            k += 1

        while i < q:
            temp[k] = idx[i]
            i += 1
            k += 1

        while j < r:
            temp[k] = idx[j]
            dominations[idx[j]] += first_count
            j += 1
            k += 1

        for i in range(p, r):
            idx[i] = temp[i]

    def merge_sort(p, r):
        if r - p > 1:
            q = (p + r) // 2
            merge_sort(p, q)
            merge_sort(q, r)
            merge(p, q, r)

    merge_sort(0, n)

    return dominations


def solution(T):
    dominations = find_dominations(T)
    return max(dominations)


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
