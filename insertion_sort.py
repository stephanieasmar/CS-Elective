# iterate over each element
# keep track of current place inn unsorted portion, andd sortedd
# iterate throgh sortedd portion, stop iterating once nextt element iis less than element that im trying to insert

# Implement the insertion sort algorithm.
# Return the sorted array.
#
# Helpful Resources
# https://www.youtube.com/watch?v=DFG-XuyPYUQ
# http://interactivepython.org/courselib/static/pythonds/SortSearch/TheInsertionSort.html
#

import datetime

def insertion_sort(array):
    for i in range(1, len(array)):
        element = array[i]
        j = i

        while (j > 0 and array[j-1] > element):
            array[j] = array[j-1]
            j = j-1

        array[j] = element

    return array


input_arrays = [
    [],
    [9, 8, 7, 6, 5, 4, 3, 2, 1],
    [1, 2, 3, 4],
    [4, 6, 1, 3, 7, 8, 4, 3, 4],
    [1],
    [1, 3, 2]
]

for array in input_arrays:
    print("")
    print(" Input: " + str(array))
    sorted_array = insertion_sort(array)
    print("Output: " + str(sorted_array))
