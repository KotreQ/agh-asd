from egz2Btesty import runtests
from math import inf as INF

def bitgame(T):
    stack = [INF]

    for move in T:
        if stack[-1] <= move:
            while stack[-1] <= move:
                stack.pop()
        else:
            stack.append(move)

    return len(stack) - 1

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( bitgame, all_tests = True )
