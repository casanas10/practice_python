class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def Solution(root):

    result = []
    result = postOrderTraversal(root, result)

    return result

def postOrderTraversal(root, result):

    if not root: return []

    postOrderTraversal(root.left, result)
    postOrderTraversal(root.right, result)

    result.append(root.val)

    return result

def postOrderTraversalNoRecursion(root):

    if not root: return []

    result = []

    stack = []

    cur = root

    while stack or cur:

        if cur:
            stack.append(cur)
            cur = cur.left
        else:
            temp = stack[-1].right
            if not temp:
                temp = stack.pop()
                result.append(temp.val)
                while stack and temp == stack[-1].right:
                    temp = stack.pop()
                    result.append(temp.val)
            else:
                cur = temp

    return result

def main():
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)

    node1.right = node2
    node2.left = node3

    root = node1
    print(postOrderTraversalNoRecursion(root))

if __name__ == "__main__":
    main()