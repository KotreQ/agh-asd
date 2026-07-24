# Bartłomiej Kochanek 430260
#
# Tworzymy sobie strukturę unionfind, gdzie każdy union ma zawarte w sobie potencjalne nagrody, które otrzyma jeśli połączy ścieżkę z odpowiednim wierzchołkiem
# Dla każdego wierzchołka, który zajmujemy, dodajemy go do uniona z każdym jego sąsiadem, który jest zajęty przez tego samego gracza i sprawdzamy, czy w obu unionach nie ma potencjalnie tej samej nagrody: jeśli jest, to stworzyliśmy ścieżkę i dostajemy nagrodę
# Dla każdej nagrody, której nie zyskaliśmy teraz, zostawiamy ją w nowo stworzonym unionie, żebyśmy mogli ją później dostać, jeśli złączymy się z drugim końcem nagrodzonej ścieżki
#
# Złożoność obliczeniowa:
# Wszystko wykonujemy raz dla każdego ruchu (rzędu V):
#   Dla każdej krawędzi od wierzchołka na którym jest ruch:
#     uf.find() - zamortyzowany czas stały
#     uf.union() - zamortyzowany czas stały
#     operacje na setach - nagród może być też rzędu V, ale za każdym razem kiedy tworzymy union tych nagród, to mamy 1 mniej set
# 
# Wydaje mi się, że O((E+V)*V), aczkolwiek jest duża szansa, że jest lepsza, ponieważ algorytm jest bardzo szybki


from zadGGtesty import runtests


class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]
    
    def find(self, a):
        if self.parent[a] != a:
            self.parent[a] = self.find(self.parent[a])
        
        return self.parent[a]
    
    def union(self, a, b):
        a = self.find(a)
        b = self.find(b)

        if a == b:
            return False
        
        if self.rank[b] > self.rank[a]:
            self.parent[a] = b
        else:
            self.parent[b] = a
            if self.rank[a] == self.rank[b]:
                self.rank[a] += 1
        
        return True


def game(G, M, W):
    NUM_PLAYERS = 2

    n = len(G)

    owner = [-1 for _ in range(n)]  # który gracz jest właścicielem wierzchołka

    rewards = [set() for _ in range(n)]  # id potencjalnych nagród, przypisanych do konkretnego union'a w unionfind'zie

    is_first_reward = [True for _ in range(NUM_PLAYERS)]  # czy to pierwsze punkty dla gracza
    player_score = [0 for _ in range(NUM_PLAYERS)]  # końcowy wynik gracza

    for i, (u, v, _) in enumerate(W):
        rewards[u].add(i)
        rewards[v].add(i)

    uf = UnionFind(n)

    for i, v in enumerate(M):
        player = i % NUM_PLAYERS
        owner[v] = player

        received_rewards = set()

        for u in G[v]:
            if owner[u] != player:  # jeśli to nie jest wierzchołek obecnego gracza, zostawiamy go
                continue

            union_a = uf.find(v)
            union_b = uf.find(u)

            if union_a == union_b: # to połącznie nie dodało nam żadnej nowej ścieżki, pomijamy
                continue

            new_received_rewards = rewards[union_a].intersection(rewards[union_b])  # które nagrody połączyliśmy
            new_union_rewards = rewards[union_a].union(rewards[union_b])  # których nie połączyliśmy, ale zapisujemy na później
            new_union_rewards.difference_update(new_received_rewards)

            uf.union(v, u)
            new_union_id = uf.find(v)
            rewards[new_union_id] = new_union_rewards  # nasz nowy union ma nagrody z obu poprzednich, minus te które dostaliśmy

            received_rewards.update(new_received_rewards)
        
        score_gained = 0
        for reward_id in received_rewards:
            _, _, reward = W[reward_id]
            score_gained += reward
        
        if score_gained > 0 and is_first_reward[player]:
            score_gained *= 2
            is_first_reward[player] = False
        
        player_score[player] += score_gained

    return tuple(player_score)


runtests(game, all_tests = True)
