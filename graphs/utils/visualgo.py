def serialize(G: list[list[int | tuple[int, int]]], directed: bool) -> str:
    result = ""
    
    n = len(G)
    m = sum(len(n) for n in G)
    if not directed:
        m //= 2
    
    result += f"{n} {m}\n"

    for v in range(n):
        for e in G[v]:
            if isinstance(e, tuple):
                u, w = e
            else:
                u = e
                w = None
            
            if not directed:
                if v > u:
                    continue
            
            result += f"{v} {u}"
            if w is not None:
                result += f" {w}"
            result += "\n"
    
    return result


def deserialize(s: str, directed: bool, weighted: bool) -> list[list[int | tuple[int, int]]]:
    lines = s.splitlines()

    n, m = map(int, lines[0].strip().split())

    G = [[] for _ in range(n)]

    for i in range(m):
        line = lines[i+1]

        if weighted:
            v, u, w = map(int, line.strip().split())
        else:
            v, u = map(int, line.strip().split())
        
        G[v].append((u, w) if weighted else u)

        if not directed:
            G[u].append((v, w) if weighted else v)
    
    return G

