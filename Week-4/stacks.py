# last in first out
# always pull from top of stack
# also a linked list

# Interface Methods:
# pop() = Removes top node from stack and returns it
# push() = Adds to top of stack
# peek() = Returns top node in stack


class Node:
    def__init__(self, value, below = None):
        self.value = value
        self.previous = below

class MyStack:
    def__init__(self):
        self.top = None
    
    def peek(self):
        return self.top

    def pop(self):
        if self.top == None:
            return None

        node_to_return = self.top
        self.top = self.top.below
        return node_to_return

    def push(self, value):
        new_node = Node(value)
        new_node.below = self.top
        self.top = new_node

