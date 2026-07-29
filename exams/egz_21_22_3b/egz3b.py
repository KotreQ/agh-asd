from egz3btesty import runtests

def maze( L ):
    # tu prosze  wpisac wlasna implementacje
    
    n = len(L)

    left = [[float("-inf") for _ in range(n)] for _ in range(n)]
    up = [[float("-inf") for _ in range(n)] for _ in range(n)]
    down = [[float("-inf") for _ in range(n)] for _ in range(n)]

    left[0][0] = 0

    for row in range(1, n):
        if L[row][0] == "#":
            break
        up[row][0] = max(left[row-1][0], up[row-1][0]) + 1

    for col in range(1, n):
        for row in range(n):
            if L[row][col] == "#":
                continue
            left[row][col] = max(left[row][col-1], up[row][col-1], down[row][col-1]) + 1

        for row in range(1, n):
            if L[row][col] == "#":
                continue
            up[row][col] = max(left[row-1][col], up[row-1][col]) + 1

        for row in range(n-2, -1, -1):
            if L[row][col] == "#":
                continue
            down[row][col] = max(left[row+1][col], down[row+1][col]) + 1

    result = max(left[n-1][n-1], up[n-1][n-1], down[n-1][n-1])
    if result == float("-inf"):
        result = -1

    return result

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( maze, all_tests = True )
