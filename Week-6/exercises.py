# First In First Out

# Interface Methods for Queues:
    # enqueue = adds the new node to end of queue
    # dequeue = retruns next node & remove it from queue
    # peek = returns next node


class Node:
    def__init__(self, value, below = None):
        self.value = value
        self.previous = below


class MyQueue:
    def__init__(self):
        self.first = None
        self.last = None

        

    def peek(self):
        #return next node
        return self.first



    def dequeue(self):
        #return next node and remove from queue
        node_to_return = self.first

        if node_to_return == self.last:
            self.last = None
            self.first = None
        else:
            self.first = self.first.previous
        
        return node_to_return


    
    def enqueue(self, value):
        #add new node to end of queue
        if self.first == None and self.last == None:
            self.first = new_node
            self.last = new_node
        else:
            self.last.previous = new_node
            self.last = new_node
