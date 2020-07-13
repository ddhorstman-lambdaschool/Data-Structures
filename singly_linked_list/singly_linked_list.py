class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_tail(self, value):
        new_node = Node(value)
        # If list is empty, new entry will be both head and tail
        if self.head is None:
            self.head = self.tail = new_node
        # If list isn't empty, append new entry to previous tail
        else:
            self.tail.set_next(new_node)
            self.tail = new_node

    def remove_head(self):
        current_head = self.head

        # Empty list
        if current_head is None:
            return None
        # Single-entry list
        elif self.head is self.tail:
            self.head = self.tail = None
        # Multiple-entry list
        else:
            self.head = current_head.get_next()

        return current_head.get_value()

    def remove_tail(self):
        current_tail = self.tail

        # Empty list
        if current_tail is None:
            return None
        # Non-empty list
        current_node = self.head
        while current_node.get_next() is not self.tail:
            current_node = current_node.get_next()
        self.tail = current_node

        return current_tail.get_value()

    def contains(self, value):
        current_node = self.head

        # Traverse all valid Nodes in the list
        while current_node:
            if current_node.get_value() is value:
                return True
            current_node = current_node.get_next()
        else:
            return False

    def get_max(self):
        if not self.head:
            return None
            
        max_value = self.head.get_value()
        current_node = self.head.get_next()

        while current_node:
            current_value = current_node.get_value()
            if current_value > max_value:
                max_value = current_value
            current_node = current_node.get_next()
        return max_value
