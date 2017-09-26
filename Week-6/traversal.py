import numpy.random as nprnd 
from binarytree import Node, show

class BSTNode(Node):
    def __init__(self, value):
        self.value = value
        self.left = none
        self.right = none

    def add(self, new_node):
        if new_node.value < self.value:
            if self.left == None:
                self.left = new_node
                new_node.parent = self
            else:
                self.left.add(new_node)
        else:
            if self.right == None:
                self.right = new_node
                new_node.parent = self
            else:
                self.right.add(new_node)

class BST:
    def __init__(self):
        self.root = None

    def add(self, value):
        new_node = BSTNode(value)

        if self.root is not None:
            self.root.add(new_node)
        else:
            self.root = new_node

    
def random_numbers(total_numbers):
    return [for i in range(total_numbers) 1]
tree = BST()
tree.add(1)
tree.add(2)
print(tree.root.value)