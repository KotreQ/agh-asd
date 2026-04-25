import sys


def dfs(G, max_diff, start, end) -> bool:
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

        return found
    
    return visit(start)


def main():
    n, m, q, d = map(int, sys.stdin.readline().strip().split())

    G = [[] for _ in range(n+1)]

    for _ in range(m):
        a, b, c = map(int, sys.stdin.readline().strip().split())
        G[a].append((b, c))
        G[b].append((a, c))

    for _ in range(q):
        v, u = map(int, sys.stdin.readline().strip().split())

        if dfs(G, d, v, u):
            print("TAK")
        else:
            print("NIE")



if __name__ == "__main__":
    main()