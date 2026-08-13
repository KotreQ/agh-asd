from egz3btesty import runtests


def kunlucky(T, k):
    # tu prosze wpisac wlasna implementacje

    n = len(T)

    is_kunlucky = [False for _ in range(n+1)]

    x = k
    i = 1
    while x <= n:
        is_kunlucky[x] = True
        x = x + (x%i) + 7
        i += 1

    start = 0
    end = 0
    kunlucky_count = 0
    result = 0

    while end < n:
        if is_kunlucky[T[end]]:
            kunlucky_count += 1
        end += 1

        while kunlucky_count > 2:
            if is_kunlucky[T[start]]:
                kunlucky_count -= 1
            start += 1

        result = max(result, end-start)

    return result
    


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( kunlucky, all_tests = True )
