# Implement the binary search.
# Return the index of the target number.
#
# Helpful Resources
# https://www.youtube.com/watch?v=D5SrAga1pno
# http://interactivepython.org/runestone/static/pythonds/SortSearch/TheBinarySearch.html
#

def binary_search_recursion(array, target):
    return -1

data = [
    [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5],
    [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3],
    [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2],
    [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 8],
]

for d in data:
    print("")
    print(" Array: " + str(d[0]))
    print("Target: " + str(d[1]))
    index_of_target = binary_search_recursion(d[0], d[1])
    print(" Index: " + str(index_of_target))
