class Node:
    """Written for you."""

    __slots__ = ("value", "next")

    def __init__(self, value, nxt=None):
        self.value = value
        self.next = nxt


class LinkedStack:

    def __init__(self):
        self._top = None
        self._size = 0


    def push(self, item):
        self._top = Node(item, self._top)
        self._size += 1


    def pop(self):
        if self.is_empty():
            raise IndexError("pop from an empty stack")
        Node = self._top
        self._top = node.next
        self._size -=1
        return node.value
    

    def peek(self):
        if self.is_empty():
             raise IndexError("peek at an empty stack")
        return self._top.value
    

    def is_empty(self):
        return self._top is None
    

    def size(self):
      return self._size
    
    def __len__(self):
        return self.size()
