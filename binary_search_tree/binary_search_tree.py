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
import sys
sys.path.extend(['/Users/elijahatkins/LambdaSchool/Data-Structures/stack','/Users/elijahatkins/LambdaSchool/Data-Structures/queue'])
from queue import Queue
from stack import Stack


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    # the left and right subtree each must also be a binary search tree
    def insert(self, value):
        # the right subtree of a node contains only nodes with a value greater than the node's value
        if value >= self.value:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BSTNode(value)
        # the Left subtree of a node contains only nodes with values lesser than the node's value
        elif value < self.value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BSTNode(value)

    def contains(self, target):
        # Return True if the tree contains the value
        if target is self.value:
            return True
        if target < self.value:
            if not self.left:
                # False if it does not
                return False
    # recursively check the tree values to left
            return self.left.contains(target)
        if target > self.value:
            if not self.right:
                # False if it does not
                return False
    # recursively check the tree values to right
            return self.right.contains(target)

   # Return the maximum value found in the tree
   # iterative aproach

    def get_max(self):
        #while loop returns first node without a right node
        while self.right:
            self = self.right
            #return the value of right most node
        return self.value

    # recursive aproach
    #this one looks for first value that doesn't have a right
    # def get_max(self):
    #     if not self.right:
    #         return self.value
    #     return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # call the function passing in the current nodes value
        fn(self.value)
        # if there is a node to the left call the function on left value
        if self.left:
            self.left.for_each(fn)
        # if there is a node on the right call the function on the right value
        if self.right:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        # loop over left side of data structure
        if self.left:
            self.left.in_order_print()
        # print all items from lowest to highest
        print(self.value)
        # loop over right side of data structure
        if self.right:
            self.right.in_order_print()

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal

    def bft_print(self):
        # make a queue
        queue = Queue()
        # enqueue the first node (self)
        queue.enqueue(self)
        # while there is data in the queue
        while queue:
            #dequeue from queue on to node
            node = queue.dequeue()
            #print current node
            print(node.value)
            #if current node_has a left child
            if node.left:
                #enqueue the left child
                queue.enqueue(node.left)
            #if current node_has a right child
            if node.right:
                #enqueue the right child
                queue.enqueue(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        # make a stack
        stack = Stack()
        #  push the node on the stack
        stack.push(self)
        # as long as the stack is not empty, put the children of the current node on the stack
        # check that they are not None, then put them on the stack
        while stack:
            node = stack.pop()
            print(node.value)
            if node.left:
                stack.push(node.left)
            if node.right:
                stack.push(node.right)

    # Stretch Goals -------------------------
    # Note: Research may be required
#https://www.techiedelight.com/preorder-tree-traversal-iterative-recursive/
    # Print Pre-order recursive DFT
    def pre_order_dft(self): 
    # Recursive function to perform pre-order traversal of the tree
    # return if the current node is empty
        if self is None:
            return
        # Display the data part of the root (or current node)
        print(self.value)
        # Traverse the left subtree
        if self.left:
            self.left.pre_order_dft()
        # Traverse the right subtree
        if self.right:
            self.right.pre_order_dft()

#https://www.techiedelight.com/postorder-tree-traversal-iterative-recursive/
    # Print Post-order recursive DFT
    def post_order_dft(self):
        pass
    # Recursive function to perform post-order traversal of the tree
    # return if the current node is empty
        if self is None:
            return
        # Traverse the left subtree
        if self.left:
            self.left.post_order_dft()
        # Traverse the right subtree
        if self.right:
            self.right.post_order_dft()
    # Display the data part of the root (or current node)
        print(self.value)


"""
This code is necessary for testing the `print` methods
"""
bst = BSTNode(1)
bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)




print("elegant methods")
print("pre order")
bst.pre_order_dft()
print("in order")
bst.in_order_print()
print("post order")
bst.post_order_dft()
