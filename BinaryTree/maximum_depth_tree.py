class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def max_depth(root):

    if not root: return 0

    left_height = max_depth(root.left)
    right_height = max_depth(root.right)

    return max(left_height, right_height) + 1

def main():
    node1 = TreeNode(3)
    node2 = TreeNode(9)
    node3 = TreeNode(20)
    node4 = TreeNode(15)
    node5 = TreeNode(7)

    node1.left = node2
    node1.right = node3
    node3.left = node4
    node3.right = node5

    root = node1
    print(max_depth(root))

if __name__ == "__main__":
    main()