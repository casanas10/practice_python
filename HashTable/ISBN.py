class DoublyLinkedNode:
    def __init__(self):
        self.isbn = 0
        self.price = 0
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity):
        self.cache = {}
        self.head = DoublyLinkedNode()
        self.tail = DoublyLinkedNode()
        self.capacity = capacity

        self.head.next = self.tail
        self.tail.prev = self.head

        self.size = 0

    def _move_to_head(self, node):
        self._remove_node(node)
        self._add_node(node)

    def _remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

        del self.cache[node.isbn]
        self.size -= 1

    def _pop_tail(self):
        self._remove_node(self.tail.prev)

    def _add_node(self, node):

        node.prev = self.head
        node.next = self.head.next

        self.head.next.prev = node
        self.head.next = node

        self.cache[node.isbn] = node
        self.size += 1

    def lookup(self, isbn):
        self._move_to_head(self.cache[isbn])
        return self.cache[isbn].price


    def insert(self, isbn, price):

        if isbn in self.cache:
            self.cache[isbn].price = price
            self._move_to_head(self.cache[isbn])
        else:
            if self.size >= self.capacity:
                self._pop_tail()

            node = DoublyLinkedNode()
            node.isbn = isbn
            node.price = price
            self._add_node(node)

    def erase(self, isbn):
        del self.cache[isbn]
        self.size -= 1

import collections

class LRUCacheOrderedDict:
    def __init__(self, capacity):
        self.cache = collections.OrderedDict()
        self.capacity = capacity

    def lookup(self, isbn):
        if isbn not in self.cache:
            return -1
        self.cache.move_to_end(isbn)
        return self.cache[isbn]


    def insert(self, isbn, price):
        if isbn in self.cache:
            self.cache.move_to_end(isbn)
        elif len(self.cache) >= self.capacity:
            self.cache.popitem(last=False)
        self.cache[isbn] = price

    def erase(self, isbn):
        return self.cache.pop(isbn) is not None


lru = LRUCache(4)    #create an LRU cache of size 4
lru.insert(1,10) #insert book isbn 1 and price 10
lru.insert(2,30)
lru.insert(3,50)
lru.insert(2, 20)
lru.insert(5,10) #insert book isbn 1 and price 10
lru.insert(10,30)
lru.insert(33,50)
lru.erase(33)    #remove book with isbn = 2
p = lru.lookup(5)   #loop up book with isbn = 1
print(p)