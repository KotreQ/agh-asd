import sys


def solution():
    in_data = sys.stdin.read().split()
    n = int(in_data[0])

    start_idxs = [int(in_data[i]) for i in range(2, 2*n+2, 2)]
    end_idxs = [int(in_data[i]) for i in range(3, 2*n+2, 2)]

    start_idxs.sort()
    end_idxs.sort()

    end_i = 0

    max_count = 0
    max_idx = 0

    count = 0

    for start_idx in start_idxs:
        while end_idxs[end_i] < start_idx:
            count -= 1
            end_i += 1

        count += 1
        if count > max_count:
            max_count = count
            max_idx = start_idx

    print(f"{max_count} {max_idx}")


if __name__ == "__main__":
    solution()


