from kol2testy import runtests

from queue import PriorityQueue


def to_adj_list(G):
    max_v = -1

    for u, v, w in G:
        max_v = max(max_v, u, v)
    
    n = max_v + 1

    new_G = [[] for _ in range(n)]

    for u, v, w in G:
        new_G[u].append((v, w))
        new_G[v].append((u, w))

    return new_G


class Node:
    def __init__(self, node_id: int, neighbours: list[int]):
        self.node_id = node_id
        self.neighbours = [[] for _ in range(17)]  # each of 17 vertices has a list of pairs: (distance, node, energy = v_id)
        self.visited = [False for _ in range(17)]

        for node, weight in neighbours:
            for start_energy in range(weight, 17):
                self.neighbours[start_energy].append((weight, node, start_energy-weight))
        
        for start_energy in range(16):
            self.neighbours[start_energy].append((8, self.node_id, 16))
    
    def visit(self, cur_energy: int, full_time: int, queue):
        if self.visited[cur_energy]:
            return
        self.visited[cur_energy] = True

        for dist, node, next_energy in self.neighbours[cur_energy]:
            queue.put((full_time + dist, node, next_energy))


def warrior(G, s, t):
    G = to_adj_list(G)
    n = len(G)

    G = [Node(i, G[i]) for i in range(n)]

    queue = PriorityQueue()  # structure in queue: (full_time, node, vertex_id = energy)

    queue.put((0, s, 16))

    while queue.qsize() > 0:
        full_time, node, cur_energy = queue.get()

        if node == t:
            return full_time
        
        G[node].visit(cur_energy, full_time, queue)




# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( warrior, all_tests = True )
