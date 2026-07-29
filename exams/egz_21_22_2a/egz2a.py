from egz2atesty import runtests


class Node:
    def __init__(self, a, b, val):
        self.a = a
        self.b = b
        self.val = val
        self.left = None
        self.right = None

def make_tree(n, val):
    def tree(p, q):
        node = Node(p, q, val)

        if p < q:
            mid = (p+q)//2
            node.left = tree(p, mid)
            node.right = tree(mid+1, q)

        return node

    return tree(0, n-1)

def update_tree(node, idx, val):
    if node.a == node.b == idx:
        node.val = val
    elif node.a <= idx <= node.b:
        a = update_tree(node.left, idx, val)
        b = update_tree(node.right, idx, val)
        node.val = max(a, b)

    return node.val

def get_first_valid(node, val):
    if val > node.val:
        return None

    if node.a == node.b:
        return node.a, node.val

    left = get_first_valid(node.left, val)
    if left is not None:
        return left
    return get_first_valid(node.right, val)

    

def coal( A, T ):
    # tu prosze wpisac wlasna implementacje
    n = len(A)
    tree = make_tree(n, T)

    for amount in A:
        idx, val = get_first_valid(tree, amount)
        update_tree(tree, idx, val-amount)

    return idx

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( coal, all_tests = True )
