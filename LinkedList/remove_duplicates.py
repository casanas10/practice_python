'''
Naive approach
for each element in the list
    check if number is repeated in the next remaining elements

O(n^2) time
O(1) space
'''
def naive_remove_duplicates(head):

    curr = head

    while curr != None:
        next = curr

        while next.next != None:
            if next.next.val == curr.val:
                next.next = next.next.next
            else:
                next = next.next

        curr = curr.next

    return head

'''
set apprach 
go through each element and store in a set
when we see a duplicate elements, remove element and continue iterating

O(n) time - only need to go through the list once
O(n) space - because we need to store each element in the list  
'''
def set_remove_duplicates(head):

    s = set()

    curr = head
    prev = None

    while curr != None:

        if curr.val in s:
            prev.next = curr.next
        else:
            s.add(curr.val)
            prev = curr

        curr = curr.next

    return head

class Node:
    def __init__(self, x):
        self.val = x
        self.next = None

def main():

    ''' Remove duplicates from Linked List
    head => 5 => 2 => 7 => 5 => 2 => None
    '''


    functions = [
        naive_remove_duplicates,
        set_remove_duplicates
    ]

    for func in functions:

        print('Problem ' + str(func))

        node1 = Node(5)
        node2 = Node(2)
        node3 = Node(7)
        node4 = Node(5)
        node5 = Node(2)

        head = node1
        node1.next = node2
        node2.next = node3
        node3.next = node4
        node4.next = node5
        node5.next = None

        head = func(head)

        # traverse the new linked list and print it
        while head != None:
            print(head.val)
            head = head.next

if __name__ == "__main__":
    main()
