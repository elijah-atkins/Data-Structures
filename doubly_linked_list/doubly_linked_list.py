"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
    

    #helper functions
    def get_value(self):
        return self.value

    def get_next(self):
        if self.next:
            return self.next
        return None
    
    def get_previous(self):
        if self.prev:
            return self.prev
        return None
    
    def delete(self):
        #check if current node has a prev and next
        #redefine previous node to point to node next to deleted one
        if self.prev:
            self.prev.next = self.next
        #redefine next node to point to node previous to deleted one
        if self.next:
            self.next.prev = self.prev
        #delete all values in node being deleted
        self.value = None
        self.next = None
        self.prev = None
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    #constructor
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    #function to return length
    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        #wrap the input value in a node
        root = ListNode(value)
        #we have a non-empty list, add the new node to the head
        if self.head and self.tail:
            #set the new node's 'next to refer to the current head
            root.next = self.head
            #set the current head's 'prev to refer to the new_node (added to make it work with DLL)
            self.head.prev = root
             # set the list's head reference to the new node  
            self.head = root
        #check if the linked list is empty
        else:
            #if the list is initially empty, set both head and tail to the new node
            self.head = root
            self.tail = root
        #increment the length
        self.length +=1
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        #check if head exist
        if self.head:
            #get head value
            headValue = self.head.get_value()
            #check to see if node has head or tail
            if self.length > 1:
                #get next head 
                newHead = self.head.get_next()
                #remove self
                self.head.delete()
                #redefine head as previously stored newHead
                self.head = newHead
                #reduce length by 1
                self.length -= 1
                #return removed item
                return headValue
            else:
                #if removing last item delete head and empty head and tail node
                self.head.delete()
                self.head = None
                self.tail = None
                #reduce length by 1
                self.length -= 1
                #return removed item
                return headValue
        #return None if no head exist
        return None
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        #wrap the input value in a node
        endNode = ListNode(value)
        if self.head and self.tail:
            endNode.prev = self.tail
            self.tail.next = endNode
            self.tail = endNode
        else:
            self.head = endNode
            self.tail = endNode
        self.length += 1
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        if self.tail:
            tailValue = self.tail.get_value()
            if self.length > 1:
                newTail = self.tail.get_previous()
                self.tail.delete()
                self.tail = newTail
                self.length -= 1
                return tailValue
            else:
                self.tail.delete()
                self.head = None
                self.tail = None
                self.length -= 1
                return tailValue
        return None
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        value = node.value
        if node == self.head:
            return
        elif node == self.tail:
            self.remove_from_tail()
            self.add_to_head(value)
        else:
            self.delete(node)
            self.add_to_head(value)
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        value = node.value
        if node == self.tail:
            return
        elif node == self.head:
            self.remove_from_head()
            self.add_to_tail(value)
        else:
            self.delete(node)
            self.add_to_tail(value)

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        if self.length == 0:
            return
        elif self.length == 1:
            self.head = None
            self.tail = None
            node.delete()
            self.length -= 1
        elif self.head == node:
            self.remove_from_head()
        elif self.tail == node:
            self.remove_from_tail()
        else:
            node.delete()
            self.length -= 1

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        if not self.head:
            return None
        max_value = self.head.value
        current_node = self.head
        while current_node:
            if current_node.value > max_value:
                max_value = current_node.value
            current_node = current_node.get_next()
        return max_value