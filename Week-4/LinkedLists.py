# How do arrays work?
# a = [1,2,3]
# a is the pointer, pointing to 1st element in array
# accessing a[0] is saying to go to memory address and offset by 0
# accessing a[1] is saying to go to memory address and offset by 1
# contiguous code = sharing common border, touching


# What is a linked lisk - how does it work?

# a = [1, 2, 3, 4, 5]

# for i in range(len(a)):
#     print hex(id(a[i]))



# LINKED LISTS: 
# Node = value, next

# linked lists do not have to be next to eachother
# tail value is empty until the next value is added
# removing from a linked list: point the next element to a different node in linked list
# no indeces, we never have to shift back in the array
# How do we search through a linked list? its more like a scavenger hunt...
# only the previous number knows where the next number is...
# you have to loop through the entire array to access each number
# inserting and deleting into a linked list happens in constant time




#inserting and deleting from a linked list:
class Node:
    def __init__(self, value):
        self.value = value
        self. next = None


class MyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        new_node = Node(value)
        #if head and tail are none,
            #if true: assign head and tail to new value
            #if false: 
                #assign the new node to current tail's next property
                #reaasign current tail to new node   

        if self.head == None and self.tail == None:
            self.head = new_node
            self.tail = new_node
        else: 
            self.tail.next = new_node
            self.tail = new_node


    def delete(self, value):
        #find the value
            #if value exists,
                #assign previous node's next property to the next node
            #else, return
        current = self.head
        while current.next != None and current.next.value != value:
            current = current.next

        my_node = current.next
        current.next = my_node.next
        my_node.next = None

        if my_node == self.tail:
            self.tail = current

        


# n1 = Node(5)
# n2 = Node(4)

# n1.next = n2

# print(n1.next.value)
# print(n2.next.value)