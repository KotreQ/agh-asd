from egzP3atesty import runtests
from math import inf

class Node:
    def __init__(self, wyborcy, koszt, fundusze):
        self.next = None
        self.wyborcy = wyborcy 
        self.koszt = koszt 
        self.fundusze = fundusze 
        self.x = None

def wybory(T):
    #tutaj proszę wpisać własną implementację

    result = 0

    for cur in T:
        fundusz = cur.fundusze

        F = [0 for _ in range(fundusz+1)]

        i = 0
        while cur is not None:
            new_F = [0 for _ in range(fundusz+1)]

            for i in range(cur.koszt):
                new_F[i] = F[i]

            for i in range(cur.koszt, fundusz + 1):
                new_F[i] = max(F[i], F[i-cur.koszt] + cur.wyborcy)

            F = new_F
            cur = cur.next
            i += 1

        result += F[-1]

    return result

runtests(wybory, all_tests = True)