from egz3btesty import runtests


def uncool( P ):
    # tu prosze wpisac wlasna implementacje
    
    F = []  # (point, index, length, is_start)
    for i, (a, b) in enumerate(P):
        F.append((a, i, b-a+1, True))
        F.append((b, i, b-a+1, False))

    def sort_key(t):
        point, index, length, is_start = t
        return (point, -length if is_start else length, index if is_start else -index)

    F.sort(key=sort_key)

    stack = []

    for point, index, length, is_start in F:
        if is_start:
            stack.append(index)
        else:
            if stack[-1] != index:
                return index, stack[-1]
            else:
                stack.pop()

    return None

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( uncool, all_tests = True )
