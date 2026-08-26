# Bartłomiej Kochanek 430260
#
# Z wszystkich czasów rozpoczęcia i zakończenia transakcji tworzymy liczby naturalne 0..n, żeby nie iterować po sekundach, w których się nic nie dzieje
# Dla każdego momentu w czasie, sprawdzamy, jaka jest maksymalna kwota jaką mogliśmy mieć po poprzednich transakcjach aż do tego momentu i na indeksie o czasie obecnej transakcji zapisujemy kwotę otrzymaną po wykonaniu także obecnej transakcji.
# Jeśli z jakiegoś powodu nie możemy wykonać transakcji (bo nie mamy wystarczającej ilości pieniędzy albo nie jest odpowiedni moment w czasie), to przepisujemy zysk z poprzedniego momentu.


from kol3_test import runtests


def transactions(M, T):
    n = len(T)

    timestamps = set()
    for s, e, _, _ in T:
        timestamps.add(s)
        timestamps.add(e)
    timestamps = sorted(timestamps)

    time2timestamp = {t: i+1 for i, t in enumerate(timestamps)}

    m = len(timestamps)

    T = [(time2timestamp[s], time2timestamp[e], p, q) for s, e, p, q in T]
    T.sort(key=lambda t: t[1])

    F = [[M for _ in range(m+1)] for _ in range(n+1)]  # F[i][j] = maksymalna posiadana kwota biorąc pod uwagę pierwsze i przedmiotów, zajmując j sekund

    for i in range(1, n+1):
        for t in range(1, m+1):
            value_if_not_taken = F[i-1][t]

            s, e, p, q = T[i-1]

            if F[i-1][s-1] >= p and t >= e:  # jeśli mamy na tyle pieniędzy, żeby wykonać transakcję i zmieścimy się w naszym czasie
                value_if_taken = F[i-1][s-1] - p + q
            else:
                value_if_taken = 0
            
            F[i][t] = max(value_if_not_taken, value_if_taken)
    
    return F[n][m]


runtests( transactions, all_tests = True)
