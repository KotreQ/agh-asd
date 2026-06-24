# Bartłomiej Kochanek 430260
#
# Z wszystkich czasów rozpoczęcia i zakończenia transakcji tworzymy liczby naturalne 0..n, żeby nie iterować po sekundach, w których się nic nie dzieje
# Dla każdego momentu w czasie, sprawdzamy, jaka jest maksymalna kwota jaką mogliśmy mieć po poprzednich transakcjach aż do tego momentu i na indeksie o czasie obecnej transakcji zapisujemy kwotę otrzymaną po wykonaniu także obecnej transakcji.
# Jeśli z jakiegoś powodu nie możemy wykonać transakcji (bo nie mamy wystarczającej ilości pieniędzy albo nie jest odpowiedni moment w czasie), to przepisujemy zysk z poprzedniego momentu.


from kol3_test import runtests


def compatible(s1, e1, s2, e2):
    return e1 < s2 or e2 < s1


def transactions(M, T):
    n = len(T)

    timesteps = set()
    for s, e, _, _ in T:
        timesteps.add(s)
        timesteps.add(e)
    timesteps = sorted(timesteps)

    time_to_step = {}
    for i, t in enumerate(timesteps):
        time_to_step[t] = i

    m = len(timesteps)

    T = [(time_to_step[s], time_to_step[e], p, q) for s, e, p, q in T]
    T.sort(key=lambda t: t[0])

    F = [[0 for _ in range(n+1)] for _ in range(m+1)]  # F[i][j] = maksymalna kwota biorąc pod uwagę pierwsze j przedmiotów, zajmując i sekund

    for i in range(n+1):
        F[i][0] = M

    for i in range(m+1):
        F[0][i] = M
    
    for i in range(1, n+1):
        for j in range(1, m+1):

            if 
    






runtests( transactions, all_tests = False)
