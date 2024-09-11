class ListNode:
    def __init__(self, key, val, prev=None, next=None):
        self.key, self.val = key, val
        self.next = next
        self.prev = prev

class LRUCache:
    #head MRU and tail LRU
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = ListNode(-1, -1)
        self.tail = ListNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.map = {}

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def insert(self, node):
        self.head.next.prev = node
        node.next = self.head.next
        node.prev = self.head
        self.head.next = node

    def get(self, key: int) -> int:
        try:
            node = self.map[key]
            self.remove(node)
            self.insert(node)
            return node.val
        except KeyError:
            return -1

    def put(self, key: int, value: int) -> None:
        if self.capacity>0:
            try:
                node = self.map[key]
                self.remove(node)
                node.val = value
                self.insert(node)
            except KeyError:
                node = ListNode(key,value)
                self.insert(node)
                self.map[key] = node
                self.capacity-=1
        else:
            try:
                node = self.map[key]
                self.remove(node)
                node.val = value
                self.insert(node)
            except KeyError:
                lruKey = self.tail.prev.key
                self.remove(self.tail.prev)
                del self.map[lruKey]
                node = ListNode(key,value)
                self.insert(node)
                self.map[key] = node
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
