"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""
# Import module from different directory
import os
import sys
parent_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(os.path.join(parent_dir, "singly_linked_list"))
sys.path.append(os.path.join(parent_dir, "stack"))
# pylint: disable=import-error
from singly_linked_list import LinkedList  # nopep8
# pylint: disable=import-error
from stack import Stack  # nopep8


# Stretch - Fancier stack implementation
class Queue:
    def __init__(self):
        self.activeStack = Stack()
        self.inactiveStack = Stack()

    def __len__(self):
        return len(self.activeStack)

    # This method puts new items on the bottom of an empty stack
    # and then flips the existing stack over on top of it.
    # Older items end up in the middle, newer ones radiate outwards.
    # For example, a 6-item stack would look like: (top) 5 3 1 2 4 6 (bottom)
    def enqueue(self, value):
        # Place on the bottom of an empty stack
        self.inactiveStack.push(value)
        # Flip the current stack over on top of new value
        for _ in range(len(self.activeStack)):
            self.inactiveStack.push(self.activeStack.pop())
        # Reverse pointers to the two stacks
        self.inactiveStack, self.activeStack = self.activeStack, self.inactiveStack

    # The oldest item is always located in the top-middle of the stack
    # It's the 3rd item in a stack of 5, 3rd in a stack of 6, 4th in a stack of 7
    # This method flips the top of the stack onto a temporary stack,
    # then extracts the middle value,
    # then flips the temporary stack back on top of the main stack.
    def dequeue(self):
        length = len(self.activeStack)
        if length is 0:
            return None
        # Flip over the (top half - 1) of the stack
        for _ in range((length-1)//2):
            self.inactiveStack.push(self.activeStack.pop())
        # Extract the middle value (which is the oldest)
        return_value = self.activeStack.pop()
        # Flip the top of the stack back over
        for _ in range(len(self.inactiveStack)):
            self.activeStack.push(self.inactiveStack.pop())
        return return_value


# Stretch - Stack implementation idea 1
# class Queue:
#     def __init__(self):
#         self.activeStack = Stack()
#         self.inactiveStack = Stack()

#     def __len__(self):
#         return len(self.activeStack)

#     def enqueue(self, value):
#         self.activeStack.push(value)

#     def dequeue(self):
#         if len(self.activeStack) is 0:
#             return None
#         elif len(self.activeStack) is 1:
#             return self.activeStack.pop()
#         else:
#             for _ in range(1, len(self.activeStack)):
#                 self.inactiveStack.push(self.activeStack.pop())
#             return_value = self.activeStack.pop()
#             for _ in range(0, len(self.inactiveStack)):
#                 self.activeStack.push(self.inactiveStack.pop())
#             return return_value

#LinkedList implementation
# class Queue:
#     def __init__(self):
#         self.size = 0
#         self.storage = LinkedList()

#     def __len__(self):
#         return self.size

#     def enqueue(self, value):
#         self.storage.add_to_tail(value)
#         self.size += 1

#     def dequeue(self):
#         if self.size is 0:
#             return None
#         self.size -= 1
#         return self.storage.remove_head()


# List (array) implementation:
# class Queue:
#     def __init__(self):
#         self.storage = []

#     def __len__(self):
#         return len(self.storage)

#     def enqueue(self, value):
#         self.storage.append(value)

#     def dequeue(self):
#         if len(self.storage) is 0:
#             return None
#         elif len(self.storage) is 1:
#             return self.storage.pop()
#         else:
#             first, *self.storage = self.storage
#             return first
