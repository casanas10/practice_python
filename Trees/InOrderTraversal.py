class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def Solution(root):

    result = []
    result = inOrderTraversal(root, result)

    return result

def inOrderTraversal(root, result):
    if not root: return []

    inOrderTraversal(root.left, result)
    result.append(root.val)
    inOrderTraversal(root.right, result)

    return result

def inOrderTraversalNoRecursion(root):

    if not root: return []
    result = []

    stack = []

    cur = root

    while cur or stack:

        while cur:
            stack.append(cur)
            cur = cur.left

        cur = stack.pop()
        result.append(cur.val)

        cur = cur.right

    return result

def main():
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)

    node1.right = node2
    node2.left = node3

    root = node1

    print(inOrderTraversalNoRecursion(root))

if __name__ == "__main__":
    main()