# 3 TREE TRAVERSAL METHODS:
# Left is always processed before right in all traversal methods: 

# 1.) Breadth First Traversal (i.e. Level Order Traversal) = Start at top, and process downward in zig-zag pattern. 
# 2.) Depth First Traversal (i.e. PostOrder) = Process the root after left and right; parent after children. RULE = left, right, root
# 3.) Depth first traversal (i.e. InOrder Traversal) RULE = left, root, right
# 4.) Preorder RULE = Root, left, right

import numpy.random as nprnd 
from binarytree import Node, show

class BSTNode(Node):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

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
    

    def print_postorder(self):
        if self.left:
            self.left.print_postorder()
        if self.right:
            self.right.print_postorder()
        print(self.value)


    def print_preorder(self):
        print(self.value)

        if self.left:
            self.left.print_preorder()

        if self.right:
            self.right.print_preorder()
    

    def print_inorder(self):
        pass

    def get_breadth_first_nodes(self):
        nodes = []
        stack = [self.root]
        while stack:
            cur_node = stack[0]
            stack = stack[1:]
            nodes.append(cur_node)

            if cur_node.left is not None:
                nodes.append(cur_node.left)

            if cur_node.right is not None:
                nodes.append(cur.node.right)
        return nodes



class BST:
    def __init__(self):
        self.root = None

    def add(self, value):
        new_node = BSTNode(value)

        if self.root is not None:
            self.root.add(new_node)
        else:
            self.root = new_node


    def print_postorder(self):
        if self.root is not None:
            self.root.print_postorder()


    def print_preorder(self):
        if self.root is not None:
            self.root.print_preorder()


    def print_inorder(self):
        if self.root is not None:
            self.root.print_inorder()


    def get_breadth_first_nodes(self):
        if self.root is not None:
            self.root.get_breadth_first_nodes

    



def random_numbers(total_numbers):
    return [int(1000 * nprnd.random()) for i in range(total_numbers)]

tree = BST();

for i in random_numbers(10):
    tree.add(i)

show(tree.root)
# tree.print_postorder()
# tree.print_preorder()
# tree.print_inorder()
tree.get_breadth_first_nodes()



