import os
import sys
parent_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(os.path.join(parent_dir, "singly_linked_list"))
# pylint: disable=import-error
from singly_linked_list import LinkedList  # nopep8

class Queue:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.storage.add_to_tail(value)
        self.size += 1

    def dequeue(self):
        if self.size is 0:
            return None
        self.size -= 1
        return self.storage.remove_head()