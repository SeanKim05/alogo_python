# class Node:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#
# class Stack:
#     def __init__(self):
#         self.top = None
#
#     def push(self, val):
#         self.top = Node(val, self.top)
#         # node = Node(val,None)
#         # node.next = self.top
#         # self.top = node
#
#     def pop(self):
#         if not self.top:
#             return None
#
#         node = self.top
#         self.top = node.next
#         return  node.val
#
#     def is_empty(self):
#         return self.top is None

class Node:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Stack:
    def __init__(self):
        self.top = None

    def push(self, val):
        node = Node(val,None)
        node.next = self.top
        self.top = node

    def pop(self):
        if not self.top:
            return None

        node = self.top
        self.top = node.next
        return node.val

    def is_empty(self):
        return self.top is None

def test_stack():
    stack = Stack()

    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)

test_stack()

    # assert stack.pop() == 5
    # assert stack.pop() == 4
    # assert stack.pop() == 3
    # assert stack.pop() == 2
    # assert stack.pop() == 1
    # assert stack.pop() is None
    # assert stack.is_empty()