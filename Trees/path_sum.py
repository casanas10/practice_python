class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def hasPathSum(root, sum):

    if not root:
        return False

    sum -= root.val

    # if we have reached a leaf node
    if not root.left and not root.right:
        return sum == 0
    return hasPathSum(root.left, sum) or hasPathSum(root.right, sum)


def stackHasPathSum(root, sum):

    if not root:
        return False

    stack = [(root, sum - root.val)]

    while stack:
        node, curr_sum = stack.pop()
        if not node.left and not node.right and curr_sum == 0:
            return True
        if node.right:
            stack.append((node.right, curr_sum - node.right.val))
        if node.left:
            stack.append((node.left, curr_sum - node.left.val))
    return False

def stringToTreeNode(input):
    input = input.strip()
    input = input[1:-1]
    if not input:
        return None

    inputValues = []
    for s in input.split(','):
        strp = s.strip()
        if strp == 'None':
            inputValues.append("null")
        else:
            inputValues.append(strp)

    root = TreeNode(int(inputValues[0]))
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1

        item = inputValues[index]
        index = index + 1
        if item != "null":
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1
        if item != "null":
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root


def main():
    line = str([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1])
    root = stringToTreeNode(line)
    sum = 22
    ret = hasPathSum(root, sum)
    print(ret)

    ret = stackHasPathSum(root, sum)
    print(ret)

if __name__ == '__main__':
    main()