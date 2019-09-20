class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def Solution(root):

    result = []
    result = preOrderTraversal(root, result)

    return result

def preOrderTraversal(root, result):
    if not root: return []

    result.append(root.val)
    preOrderTraversal(root.left, result)
    preOrderTraversal(root.right, result)

    return result

def preOrderTraversalNoRecursion(root):

    if not root: return []
    result = []

    stack = [root]

    while stack:
        root = stack.pop()

        if root:
            result.append(root.val)
            if root.right:
                stack.append(root.right)
            if root.left:
                stack.append(root.left)

    return result

def main():
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)

    node1.right = node2
    node2.left = node3

    root = node1

    print(preOrderTraversalNoRecursion(root))

if __name__ == "__main__":
    main()