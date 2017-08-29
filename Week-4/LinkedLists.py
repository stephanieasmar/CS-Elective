# How do arrays work?
# a = [1,2,3]
# a is the pointer, pointing to 1st element in array
# accessing a[0] is saying to go to memory address and offset by 0
# accessing a[1] is saying to go to memory address and offset by 1
# contiguous code = sharing common border, touching


# What is a linked lisk - how does it work?

a = [1, 2, 3, 4, 5]

for i in range(len(a)):
    print hex(id(a[i]))



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