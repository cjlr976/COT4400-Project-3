"""
Purpose: Creates deque for BFS using a doubly linked list
* Used to keep track of hospitals that are waiting to be explored
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class Deque:
    def __init__(self):
        self.head = None
        self.tail = None

    # insert at back
    def append(self, value):
        new_node = Node(value)

        if self.tail is None:  # empty deque
            self.head = self.tail = new_node
            return

        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node

    # remove from front
    def popleft(self):
        if self.head is None:
            return None

        value = self.head.value
        self.head = self.head.next

        if self.head is None:  # became empty
            self.tail = None
        else:
            self.head.prev = None

        return value

    def is_empty(self):
        return self.head is None