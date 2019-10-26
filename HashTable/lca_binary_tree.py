class TreeNode:
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None

def LCA(root, node0, node1):
    nodes_on_path = set()
    iter0, iter1 = node0, node1
    while iter0 or iter1:
        if iter0:
            if iter0 in nodes_on_path:
                return iter0
            nodes_on_path.add(iter0)
            iter0 = iter0.parent
        if iter1:
            if iter1 in nodes_on_path:
                return iter1
            nodes_on_path.add(iter1)
            iter1 = iter1.parent


n1 = TreeNode(3)
n2 = TreeNode(6)
n3 = TreeNode(8)
n4 = TreeNode(2)
n5 = TreeNode(11)
n6 = TreeNode(13)
n7 = TreeNode(9)
n8 = TreeNode(5)
n9 = TreeNode(17)

n1.parent = None
n1.left = n2
n1.right = n3

n2.parent = n1
n2.left = n4
n2.right = n5

n3.parent = n1
n3.left = None
n3.right = n6

n4.parent = n2

n5.parent = n2
n5.left = n7
n5.right = n8

n6.parent = n3

n7.parent = n5

n8.parent = n5

n9.parent = n6

val = LCA(n1, n9, n3)

print(val.key)