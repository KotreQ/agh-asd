import sys
import array


def select_pivot(A, p, r):
    if r - p <= 3:
        return p

    a = p
    b = (p+r) // 2
    c = r

    if A[a] < A[b]:
        if A[b] < A[c]:
            return b
        elif A[c] < A[a]:
            return a
        else:
            return c
    else:
        if A[a] < A[c]:
            return a
        elif A[c] < A[b]:
            return b
        else:
            return c


def partition(A, p, r):
    pivot_idx = select_pivot(A, p, r)
    pivot = A[pivot_idx]

    # move pivot to end
    A[r], A[pivot_idx] = A[pivot_idx], A[r]

    i = p
    j = r - 1

    while i <= j:
        if A[i] > pivot and A[j] < pivot:
            A[i], A[j] = A[j], A[i]

        if A[i] <= pivot:
            i += 1

        if A[j] >= pivot:
            j -= 1

    # move pivot to correct index
    A[r], A[i] = A[i], A[r]

    return i


class Tree:
    def __init__(self):
        self.root = None

    def add(self, idx):
        new_node = Node(idx)

        if self.root is None:
            self.root = new_node
            return
        
        cur = self.root
        while True:
            if idx < cur.idx:
                if cur.left is not None:
                    cur = cur.left
                else:
                    cur.left = new_node
                    new_node.parent = cur
                    return

            elif idx > cur.idx:
                if cur.right is not None:
                    cur = cur.right
                else:
                    cur.right = new_node
                    new_node.parent = cur
                    return

            else:
                return
        
    def search(self, idx):
        cur = self.root
        if cur is None:
            return None

        while True:
            if idx == cur.idx:
                return cur

            if idx < cur.idx and cur.left is not None:
                cur = cur.left
            elif idx > cur.idx and cur.right is not None:
                cur = cur.right
            else:
                break

        return cur

    def search_range(self, idx):
        found = self.search(idx)

        if found is None:
            return None, None

        if found.idx < idx:
            right = found.next(True)
            return found.idx, right.idx if right is not None else None
            
        elif found.idx > idx:
            left = found.next(False)
            return left.idx if left is not None else None, found.idx

        return found.idx, found.idx

    def print(self):
        from queue import Queue
        q = Queue()

        print(10*"-")
        if self.root is None:
            print("TREE EMPTY")
        else:
            print("TREE:")
            q.put((0, self.root))

            last_level = 0
            while q.qsize() > 0:
                level, cur = q.get()
                if cur.left is not None:
                    q.put((level+1, cur.left))
                if cur.right is not None:
                    q.put((level+1, cur.right))
                
                if level > last_level:
                    last_level = level
                    print("")
                print(cur.idx, end=" ")
            print("")
        print(10*"-")

class Node:
    def __init__(self, idx):
        self.idx = idx
        self.parent = None
        self.left = None
        self.right = None
    
    def next(self, right: bool):
        # if right node exists, get its leftmost child
        if (self.right if right else self.left) is not None:
            cur = self.right if right else self.left

            while (cur.left if right else cur.right) is not None:
                cur = cur.left if right else cur.right
            
            return cur

        # if node has no right node, search parents until it's parent's left node
        else:
            cur = self
            p = cur.parent

            while p is not None and cur is (p.right if right else p.left):
                cur = p
                p = p.parent

            return p


def main():
    n = int(sys.stdin.readline().strip())
    T = array.array('L', (int(input().strip()) for _ in range(n)))

    q = int(sys.stdin.readline().strip())
    
    bst_cache = Tree()

    for _ in range(q):
        idx = n - int(input())
        
        bst_cache.print()
        a, b = bst_cache.search_range(idx)
        if a is None:
            a = 0
        if b is None:
            b = n-1

        found = a-1
        while found != idx:
            if found < idx:
                a = found + 1
            elif found > idx:
                b = found - 1

            found = partition(T, a, b)
            bst_cache.add(found)

        print(T[found])


if __name__ == "__main__":
    main()
