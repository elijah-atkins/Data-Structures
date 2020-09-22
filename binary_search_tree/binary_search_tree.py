"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    #helper function 
    def get_next(self):
        if self.right:
            return self.right
        return None

    # Insert the given value into the tree
        #the left and right subtree each must also be a binary search tree
    def insert(self, value):
        #the right subtree of a node contains only nodes with a value greater than the node's value
        if value >= self.value:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BSTNode(value)
        #the Left subtree of a node contains only nodes with values lesser than the node's value
        elif value < self.value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BSTNode(value)



    def contains(self, target):
    # Return True if the tree contains the value
        if target is self.value:
            return True
    # False if it does not
        if target <= self.value:
            if self.left is None:
                return False
    # recursively check the tree values
            return self.left.contains(target)
        if target > self.value:
            if self.right is None:
                return False
            return self.right.contains(target)


   #Return the maximum value found in the tree
    def get_max(self):
        #check if node has items to right and left if not return value in node
        if not self.right:
            return self.value
        #set initial max value as value of self
        max_value = self.value
        #start at head
        current_node = self
        while current_node:
            if current_node.value > max_value:
                #check value in current node if greater than 
                #max_value set current value as new max
                max_value = current_node.value
            #cycle to next node
            current_node = current_node.get_next()
        #return higest value
        return max_value




        #recursive 
    # def get_max(self):

    #     if self.right is None:
    #         return self.value
    #     return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        #call the function passing in the current nodes value
        fn(self.value)
        #if there is a node to the left call the function on left value
        if self.left:
            self.left.for_each(fn)
        #if there is a node on the right call the function on the right value
        if self.right:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        if self.left:
            self.left.in_order_print()
        print(self.value)
        if self.right:
            self.right.in_order_print()

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self):
        pass

"""
This code is necessary for testing the `print` methods
"""
bst = BSTNode(10)

bst.insert(2)
bst.insert(1)
bst.insert(3)
bst.insert(4)
bst.bft_print()
bst.dft_print()
print("Max")
print(bst.get_max())




print("elegant methods")
print("pre order")
bst.pre_order_dft()
print("in order")
bst.in_order_print()
print("post order")
bst.post_order_dft()  
