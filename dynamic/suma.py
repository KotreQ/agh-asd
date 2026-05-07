# Czy istnieje pociąg liczb z A[] który sumuje się do T

from pprint import pprint


A = [5,2,4,20,5,40]
T = 12


def suma(A, T):
    # dp[n, s] -> czy da się z n pierwszych elementów stworzyć sumę s
    dp = [[False for _ in range(T+1)] for _ in range(len(A)+1)]

    N = len(A)
    
    for i in range(N+1):
        dp[i][0] = True
    
    for n in range(1, N+1):
        for s in range(1, T+1):
            dp[n][s] = dp[n-1][s] or (s >= A[n-1] and dp[n-1][s-A[n-1]])
    
    for row in dp:
        print(list(map(int, row)))

    return dp[N][T]


print(suma(A, T))
