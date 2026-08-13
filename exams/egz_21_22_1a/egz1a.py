from egz1atesty import runtests

def snow( S ):
    # tu prosze wpisac wlasna implementacje

    S.sort(reverse=True)

    result = 0
    day = 0
    for val in S:
        val -= day
        if val <= 0:
            break

        result += val
        day += 1

    return result

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( snow, all_tests = True )
