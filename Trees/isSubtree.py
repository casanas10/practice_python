'''
Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s.
A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.
Given tree s:
     3
    / \
   4   5
  / \
 1   2

 Given tree t:
   4
  / \
 1   2

Return true, because t has the same structure and node values with a subtree of s.

'''
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def isSubtree(s, t):

    ##EDGE CASES
    if t == None: return False
    if s == None: return True

    def isMatch(s, t):
        if s == None and t == None: return True
        if s == None or t == None: return False

        if s.val != t.val:
            return False

        return isMatch(s.left, t.left) and isMatch(s.right, t.right)

    if isMatch(s,t):
        return True

    return isSubtree(s.left, t) or isSubtree(s.right, t)


node1 = TreeNode(3)
node2 = TreeNode(4)
node3 = TreeNode(5)
node4 = TreeNode(1)
node5 = TreeNode(2)

s = node1
node1.left = node2
node1.right = node3

node2.left = node4
node2.right = node5


node6 = TreeNode(4)
node7 = TreeNode(1)
node8 = TreeNode(2)
t = node6
node6.left = node7
node6.right = node8

print(isSubtree(s, t))