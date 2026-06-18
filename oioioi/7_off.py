def main():
    p = 1000696969

    n, m, A, B = map(int, input().strip().split())
    n -= 1
    m -= 1
    F = []  # F[k][x][y]

    F.append([[0 for _ in range(m)] for _ in range(n)])
    F[0][0][0] = 1

    query_count = int(input().strip())
    for _ in range(query_count):
        in_k, in_x, in_y = map(int, input().strip().split())
        in_x -= 1
        in_y -= 1

        for k in range(len(F), in_k+1):
            F.append([[0 for _ in range(m)] for _ in range(n)])

            for x in range(n):
                for y in range(m):
                    F[k][x][y] = F[k-1][x][y]

                    for a in range(1, min(A+1, x+1)):
                        F[k][x][y] += F[k-1][x-a][y]

                    for b in range(1, min(B+1, y+1)):
                        F[k][x][y] += F[k-1][x][y-b]

                    F[k][x][y] %= p
        
        print(F[in_k][in_x][in_y])


if __name__ == "__main__":
    main()