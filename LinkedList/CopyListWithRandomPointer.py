'''
Problem:
A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.
'''

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.random = None


'''
Approach 1 - Recursive Approach 
Time Complexity O(n)
Space Complexity O(n)
'''
def copyRandomList(head):

    visited = {}

    def helper(head):
        if head == None:
            return None

        if head in visited:
            return visited[head]

        node = ListNode(head.val)
        visited[head] = node

        node.next = helper(head.next)
        node.random = helper(head.random)

        return node

    return helper(head)


'''
Approach 2 Iterative Approach 
Time Complexity O(n)
Space Complexity O(n)
'''
def getClonedNode(node, visited):
    # If node exists then
    if node:
        # Check if its in the visited dictionary
        if node in visited:
            # If its in the visited dictionary then return the new node reference from the dictionary
            return visited[node]
        else:
            # Otherwise create a new node, save the reference in the visited dictionary and return it.
            visited[node] = ListNode(node.val)
            return visited[node]
    return None

def copyRandomList_Approach2(head):

    visited = {}

    if not head:
        return head

    old_node = head
    # Creating the new head node.
    new_node = ListNode(old_node.val)
    visited[old_node] = new_node

    # Iterate on the linked list until all nodes are cloned.
    while old_node != None:
        # Get the clones of the nodes referenced by random and next pointers.
        new_node.random = getClonedNode(old_node.random, visited)
        new_node.next = getClonedNode(old_node.next, visited)

        # Move one step ahead in the linked list.
        old_node = old_node.next
        new_node = new_node.next

    return visited[head]


node1 = ListNode(4)
node2 = ListNode(7)
node3 = ListNode(-2)

head = node1
node1.next = node2
node1.random = node3

node2.next = node3
node2.random = node1

node3.next = None
node3.random = None

# node = copyRandomList(head)
# print(node)

node = copyRandomList_Approach2(head)
print(node)