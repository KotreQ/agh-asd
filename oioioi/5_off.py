import sys


class UnionFind:
    def __init__(self, N):
        self.N = N
        self.parent = [n for n in range(N)]
        self.rank = [0 for _ in range(N)]
    
    def union(self, a, b):
        a = self.find(a)
        b = self.find(b)

        if a == b:
            return False
        
        if self.rank[a] < self.rank[b]:
            self.parent[a] = b
        else:
            self.parent[b] = a
            if self.rank[a] == self.rank[b]:
                self.rank[a] += 1

    def find(self, a):
        if a == self.parent[a]:
            return a
        
        self.parent[a] = self.find(self.parent[a])

        return self.parent[a]
    
    def in_union(self, a, b):
        return self.find(a) == self.find(b)
    

def dfs(G, max_diff, start, end, cache) -> bool:
    visited = [False for _ in range(len(G))]

    def visit(i, min_val_inh = None, max_val_inh = None):
        if i == end:
            return True
        
        visited[i] = True

        found = False


        for neigh, val in G[i]:
            min_val = min_val_inh
            max_val = max_val_inh
            if min_val is None or val < min_val:
                min_val = val
            if max_val is None or val > max_val:
                max_val = val

            distance_valid = (max_val - min_val) <= max_diff

            if distance_valid and not visited[neigh]:
                if visit(neigh, min_val, max_val):
                    found = True
                    break
                    
        visited[i] = False

        if found:
            cache[end].add(start)

        return found
    
    if start in cache[end]:
        return True

    return visit(start)


def main():
    n, m, q, d = map(int, sys.stdin.readline().strip().split())

    G = [[] for _ in range(n+1)]

    for _ in range(m):
        a, b, c = map(int, sys.stdin.readline().strip().split())
        G[a].append((b, c))
        G[b].append((a, c))

    cache = [set() for _ in range(n+1)]  # cache[n] = set of items the n-th item is reachable from

    for _ in range(q):
        v, u = map(int, sys.stdin.readline().strip().split())

        if dfs(G, d, v, u, cache):
            print("TAK")
        else:
            print("NIE")



if __name__ == "__main__":
    main()