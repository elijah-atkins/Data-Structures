"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass."""

class Stack:
    #constructor
    def __init__(self):
        #initializing attributes of stack
        #only need an array because it alrady has a len function
        self.storage = []

    #defining stack __len__ method 
    def __len__(self):
        #return lenght of array
        return len(self.storage)

    #defining push method to add item
    def push(self, value):
        #add value to end of array
        self.storage.append(value)
        #return full array
        return self.storage

    #defining pop method to remove value
    def pop(self):
        #if array is empty return None
        if len(self.storage) == 0:
            return None
        #if array is not empty remove and return last item in array      
        return self.storage.pop()
    #define peek method to show storage value at end of array  
    def peek(self):
        return self.storage[-1]

"""
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass."""

from singly_linked_list import LinkedList
class Stack:
    #constrctor
    def __init__(self):
        #initialize the attributes of stack
        self.size = 0
        #create storage from LinkedList
        self.storage = LinkedList()

    #defining stack __len__ method
    def __len__(self):
        #return object attribute size
        return self.size

    #define push method to add value
    def push(self, value):
        #use method in linked list to store value in head
        self.storage.add_to_head(value)
        #increase storage size by 1
        self.size += 1
        #return the full array
        return self.storage

    #define pop method to remove value
    def pop(self):
        if self.size == 0:
            return None
        self.size -= 1
        #use method in linked list to remove value
        #removing from head because push function adds to head for
        #First in first out behavior
        return self.storage.remove_head()
    
    #define peek to show contents of storage
    def peek(self):
        return self.storage.
"""
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?

   An array keeps all of its memory together as a big block
   vs. a linked list where the memory is assigned and data can be refrenced by pointing to certain spots in memory
"""