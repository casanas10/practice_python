class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def sortedArrayToBST(nums):
    if not nums:
        return None

    mid = (len(nums) - 1) // 2
    root = TreeNode(nums[mid])
    root.left = sortedArrayToBST(nums[:mid])
    root.right = sortedArrayToBST(nums[mid+1:])

    return root

def optimalSortedArrayToBST(self, nums):
    # Time: O(n)
    # Space: O(n) in the case of skewed binary tree.
    def convert(left, right):
        if left > right:
            return None
        mid = (left + right) // 2
        node = TreeNode(nums[mid])
        node.left = convert(left, mid - 1)
        node.right = convert(mid + 1, right)
        return node
    return convert(0, len(nums) - 1)

def main():
    nums = [-10,-3,0,5,9]
    ret = sortedArrayToBST(nums)

if __name__ == '__main__':
    main()