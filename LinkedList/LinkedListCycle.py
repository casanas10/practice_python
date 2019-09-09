class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def hasCycle(head):

    s = set()

    cur = head

    while cur:
        if cur in s:
            return True

        s.add(cur)
        cur = cur.next

    return False

def two_pointer_solution(head):

    if not head or not head.next:
        return False

    slow = head
    fast = head.next

    while slow != fast:
        if not fast or not fast.next:
            return False

        slow = slow.next
        fast = fast.next.next

    return True


def main():
    node1 = ListNode(3)
    node2 = ListNode(2)
    node3 = ListNode(0)
    node4 = ListNode(-4)

    head = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2

    print(two_pointer_solution(head))


if __name__ == "__main__":
    main()