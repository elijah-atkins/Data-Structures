"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass."""

# class Queue:
#     def __init__(self):
#         self.storage = []
    
#     def __len__(self):
#         return len(self.storage)

#     def enqueue(self, value):
#         return self.storage.append(value)

#     def dequeue(self):
#         if len(self.storage) == 0:
#             return None
#         return self.storage.pop(0)
"""
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass."""

# from singly_linked_list import LinkedList

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
#         if self.size == 0:
#             return None
#         self.size -= 1
#         return self.storage.remove_head()

"""
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?

   	   An array would be considered Linear O(n) because as the array grows so do the # of operations. 
        A linked list would be faster, it can be represented by O(1).
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
         I needed two stacks
"""

#Stretch: Queue (using a stack)

from stack import Stack

class Queue:
    def __init__(self):
        self.size = 0
        self.storage = Stack()
        self.temp_storage = Stack()

    # len performance: O(1)
    def __len__(self):
        return self.size

    # enqueue performance: O(1)
    def enqueue(self, value):
        self.storage.push(value)
        self.size += 1

    # dequeue performance: O(n)
    def dequeue(self):
        if self.size == 0:
            return None

        self.size -= 1

        # take all but one item out of storage stack and put values in temp_storage stack
        while len(self.storage) > 1:
            self.temp_storage.push(self.storage.pop())
        # remove last item from storage stack and store and elem_popped
        elem_popped = self.storage.pop()

        # take all items out of temp_storage stack and put them back in storage stack
        while len(self.temp_storage) > 0:
            self.storage.push(self.temp_storage.pop())

        return elem_popped 