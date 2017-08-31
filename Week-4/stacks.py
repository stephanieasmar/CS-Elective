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
        pass

    def pop(self):
        pass

    def push(self, value):
        pass

