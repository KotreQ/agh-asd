
F = [1, 2, 7]

def main():
    n = int(input())

    for _ in range(n):
        q = int(input())-1

        if len(F) <= q:
            for i in range(len(F), q+1):
                F.append((3*F[i-1] + F[i-2] - F[i-3]) % 67)
        
        print(F[q])



if __name__ == "__main__":
    main()