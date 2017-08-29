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