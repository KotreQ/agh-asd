# Bartłomiej Kochanek 430260
# 
# Klasyczny problem plecakowy z dodatkowym jednym wymiarem.
# Dla każdej możliwej ilości egzaminów i dla każdego możliwego obłożenia obu sal mamy trzy możliwości:
# - możemy nie przeprowadzać tego egzaminu i wziąć wartość z poprzednich egzaminów przy takim samym obłożeniu
# - możemy przeprowadzić go w sali nr 1 i wziąć wartość z poprzednich egzaminów, jeśli sala nr 1 była już dostępna w czasie startu obecnego
# - analogicznie dla sali nr 2
# i wziąć największą wartość z tych trzech możliwości
#
# Żeby polepszyć złożonośc obliczeniową algorytmu, zamieniamy każdy czas rozpoczęcia i zakończenia egzaminu na konkretny timestamp, ponieważ nie musimy brać pod uwagę czasu, w którym nie może się rozpocząć lub zakończyć żaden egzamin.
# Takich timestampów jest maksymalnie 2N, czyli rzędu N, więc złożoność O(N*T^2) zamienia się w O(N^3)
#
# Złożoność obliczeniowa: O(N^3)


from zadSiEtesty import runtests


def sale_i_egzaminy(E):
    n = len(E)

    timestamps = set()
    
    for s, e, _ in E:
        timestamps.add(s)
        timestamps.add(e)
    
    timestamps.add(0)
    timestamps = sorted(timestamps)
    time2timestamp = {t: i+1 for i, t in enumerate(timestamps)}

    T = len(timestamps)

    # F[i][t1][t2] = ile maksymalnie studentów może być przeegzaminowanych, biorąc pod uwagę pierwsze i egzaminów, gdzie sala nr 1 jest zajęta maksymalnie do czasu t1, a sala 2 maksymalnie do czasu t2
    F = [[[0 for _ in range(T+1)] for _ in range(T+1)] for _ in range(n+1)]

    for i in range(1, n+1):
        start, end, value = E[i-1]
        start = time2timestamp[start]
        end = time2timestamp[end]

        for t1 in range(1, T+1):
            for t2 in range(1, T+1):
                value_not_taken = F[i-1][t1][t2]
                value_taken_1 = value + F[i-1][start-1][t2] if end <= t1 else 0
                value_taken_2 = value + F[i-1][t1][start-1] if end <= t2 else 0

                F[i][t1][t2] = max(value_not_taken, value_taken_1, value_taken_2)
        
    return F[n][T][T]

runtests(sale_i_egzaminy, all_tests=True)
