# Bartłomiej Kochanek 430260
#
# Opis algorytmu:
# Skoro k-ty najmniejszy spośród elementów T[0] ... T[i] musi być niemniejszy od x, to oznacza że w tym przedziale może być k-1 elementów mniejszych od x
# Iterujemy przez tablicę, liczymy ile elementów jest mniejszych od wartości x i dopóki ta wartość nie przekracza dopuszczalnej oraz jest niemniejsza od k-1 (bo w mniejszej tablicy nie ma k-tego elementu) to zapisujemy i jako poprawny wynik, tak szukając największego odpowiedniego i
# Z tego też wynika, że jeśli jakaś wartość i jest niepoprawna, to każda większa też na pewno będzie niepoprawna
# 
# Złożoność obliczeniowa: O(n)
# Złożoność pamięciowa: O(1)


from zadKTtesty import runtests

def kth(T, x, k):
    # tu prosze wpisac wlasna implementacje

    n = len(T)

    result = -1
    smaller_count = 0
    for i in range(n):

        if T[i] < x:
            smaller_count += 1

        if smaller_count >= k:
            break

        if i >= k - 1:
            result = i

    return result

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( kth, all_tests = True )
