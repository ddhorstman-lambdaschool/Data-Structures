"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next

    def __repr__(self):
        return f"<ListNode: {self.value} >"


"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node else 0

    def __len__(self):
        return self.length

    def __repr__(self):
        rep = f"< DoublyLinkedList ({self.length}):"
        current = self.head
        while current:
            rep += f"\n {current}"
            current = current.next
        rep += "\n>"
        return rep
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """

    def add_to_head(self, value):
        new_node = ListNode(value, next=self.head or None)
        # Non-empty list: old head points to new head
        if self.head:
            self.head.prev = new_node
        # Empty list: new head is also new tail
        else:
            self.tail = new_node
        self.head = new_node
        self.length += 1

    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """

    def remove_from_head(self):
        old_head = self.head
        # Empty list: no-op
        if not old_head:
            return None
        # Single-element list: empty out list
        if old_head is self.tail:
            self.tail = self.head = None
        # Multi-element list: assign new head
        else:
            self.head = old_head.next
            self.head.prev = None
        self.length -= 1
        return old_head.value

    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """

    def add_to_tail(self, value):
        new_node = ListNode(value, prev=self.tail or None)
        # Non-empty list: old tail points to new tail
        if self.tail:
            self.tail.next = new_node
        # Empty list: new tail is also new head
        else:
            self.head = new_node
        self.tail = new_node
        self.length += 1

    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """

    def remove_from_tail(self):
        old_tail = self.tail
        # Empty list: no-op
        if not old_tail:
            return None
        # Single-element list: empty out list
        if old_tail is self.head:
            self.tail = self.head = None
        # Multi-element list: assign new tail
        else:
            self.tail = old_tail.prev
            self.tail.prev = None
        self.length -= 1
        return old_tail.value

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """

    def move_to_front(self, node):
        # One element or first element: no-op
        if self.length == 1 or not node or not node.prev:
            return
        # Last element: update tail
        if node is self.tail:
            self.tail = node.prev
        # Not last: next element points to prev
        else:
            node.next.prev = node.prev
        # Update ref from prev, remove, and re-add to head
        node.prev.next = node.next
        self.length -= 1
        self.add_to_head(node.value)

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """

    def move_to_end(self, node):
        # One element or last element: no-op
        if self.length == 1 or not node or not node.next:
            return
        # First element: update head
        if node is self.head:
            self.head = node.next
        # Not first: prev points to next
        else:
            node.prev.next = node.next
        # Update ref from next, remove, and re-add to tail
        node.next.prev = node.prev
        self.length -= 1
        self.add_to_tail(node.value)

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """

    def delete(self, node):
        # No node: no-op
        if not node:
            return None
        # One element: clear list
        if self.length == 1:
            self.head = self.tail = None
            self.length = 0
            return node.value
        # Multiple elements:
        self.length -= 1
        if self.head is node:
            self.head = node.next
        else:
            node.prev.next = node.next
        if self.tail is node:
            self.tail = node.prev
        else:
            node.next.prev = node.prev
        return node.value

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """

    def get_max(self):
        max = 0 if self.head else None
        current = self.head
        while current:
            if current.value > max:
                max = current.value
            current = current.next
        return max
