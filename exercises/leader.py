import random
from collections import defaultdict


def count_occurrences(A, x):
    res = 0
    for e in A:
        if e == x:
            res += 1
    
    return res

def find_leader(A):
    count = 0
    candidate = None

    for e in A:
        if candidate == e:
            count += 1
        else:
            count -= 1
            if count < 0:
                candidate = e
                count = 1
    
    if count > 0 and count_occurrences(A, candidate) > len(A) // 2:
        return candidate
    return None

def find_leader_slow(A):
    counts = defaultdict(int)

    n = len(A)

    for e in A:
        counts[e] += 1
    
    max_elem = max(counts, key= lambda e: counts[e])
    max_count = counts[max_elem]

    if max_count > n//2:
        return max_elem
    return None



def main() -> None:
    RANDOM_RANGE = (0, 99)
    TEST_SIZE_RANGE = (10, 40)
    POSITIVE_PROBABILITY = 0.1
    TEST_COUNT = 10000

    TEST_DATA = []

    for _ in range(TEST_COUNT):
        n = random.randint(*TEST_SIZE_RANGE)
        A = [random.randint(*RANDOM_RANGE) for _ in range(n)]

        if random.random() < POSITIVE_PROBABILITY:
            leader = random.randint(*RANDOM_RANGE)
            leader_count = random.randint(n//2 + 1, n)
            for i in random.sample(range(n), leader_count):
                A[i] = leader
        
        TEST_DATA.append(A)
    
    for A in TEST_DATA:
        res1 = find_leader(A)
        res2 = find_leader_slow(A)

        print(f"DATA: {A}")
        print(f"RESULT 1: {res1}")
        print(f"RESULT 2: {res2}")

        if res1 != res2:
            print("ERROR")

        print("")


if __name__ == "__main__":
    main()