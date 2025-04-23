class HashNode:
    def __init__(self,key, val):
        self.key = key
        self.val = val
        self.next = None

class HashTable:
    def __init__(self):
        self.size = 10
        self.table = [None] * self.size

    def hash_func(self,key):
        return key % self.size

    def put(self, key, val):
        index = self.hash_func(key)
        if self.table[index] is None:
            self.table[index] = HashNode(key, val)
        else:
            node = self.table[index]
            while node.next is not None:
                node = node.next
            node.next = HashNode(key, val)

    def get(self, key):
        index = self.hash_func(key)
        node = self.table[index]
        while node is not None:
            if node.key == key:
                return node.val
            node = node.next
        return -1

    def remove(self, key):
        index = self.hash_func(key)
        node = self.table[index]
        prev_node = None
        while node is not None:
            if node.key == key:
                if prev_node is None:
                    self.table[index] = node.next
                else:
                    prev_node.next = node.next
                return
            prev_node = node
            node = node.next


