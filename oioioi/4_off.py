import sys
from queue import PriorityQueue


def main():
    n, m, k = map(int, sys.stdin.readline().strip().split())

    edges = [[] for _ in range(n+1)]

    parents = [None for _ in range(n+1)]
    min_costs = [float("inf") for _ in range(n+1)]
    path_lens = [float("inf") for _ in range(n+1)]
    visited = [False for _ in range(n+1)]

    for _  in range(m):
        a, b, c = map(int, sys.stdin.readline().strip().split())
        edges[a].append((b, c))
        edges[b].append((a, c))


    q = PriorityQueue()
    q.put((1, 1, 0))  # full_cost, node, parent

    def visit():
        full_cost, node, parent = q.get()

        if visited[node]:
            return
        visited[node] = True

        min_costs[node] = full_cost
        parents[node] = parent

        for child, cost in edges[node]:
            child_full_cost = full_cost * cost
            q.put((child_full_cost, child, node))
    
    

    for _ in range(k):
        target = int(sys.stdin.readline().strip())

        while not visited[target]:
            visit()

        path = [str(target)]
        cur = target
        while cur != 1:
            cur = parents[cur]
            path.append(str(cur))
        
        path = path[::-1]

        print(f"{len(path)} {' '.join(path)} {min_costs[target]}")


if __name__ == "__main__":
    main()