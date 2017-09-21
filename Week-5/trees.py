# Think of trees like linked lists - association is parent/child instead of linear
# Binary tree = each tree has max 2 children (left and right children)
# Binary search tree = binary tree with a single rule, if you look at nodes to right of a node, they are all >, look at nodes to left, they are all <

Best case scenario: O(log n)
# Not constant time, but close, and nowhere near as bad as linear growth

Worst case scenario: O(n)
# Linear growth


# Today's Class (Day 10):
# sets
# Recursive objects
# Deleting object from tree
# Unbalanced trees


# 1.) SETS:
# A data structure, similar to an array but....cannot contain duplicates, and is unordered.
# Uses hashing to do lookups in constant time



# 2.) RECURSIVE OBJECTS:
# An object that has a reference to another object of the same type



# 3.) DELETING OBJECTS FROM TREES:
# node is a leaf with no children: you can simply remove the associateion between parent and child
# node is a leaf with 1 child: we remove the node by setting the node's child's parent to n parent (i.e. set the child's parent's pointer to the new child node), and the new parent's child to the new child
# node is a leaf with 2 children:


# 4.) UNBALANCED TREES:
# A tree with subtrees that have a difference in height tht is greater than one
