# Implement the bubble sort algorithm in the bubble_sort method.
# Return the sorted array.
#
# Helpful Resources
# https://www.youtube.com/watch?v=8Kp-8OGwphY
# http://interactivepython.org/runestone/static/pythonds/SortSearch/TheBubbleSort.html
#

def bubble_sort(my_arr):
    swapped = True
    while swapped == True:
        swapped = False
        for i in range(len(my_arr)-1):
            if my_arr[i] > my_arr[i+1]:
                my_arr[i], my_arr[i+1] = my_arr[i+1], my_arr[i]
                swapped == True
    return my_arr

print bubble_sort([1,3,2,5,6])



# input_arrays = [
#     [],
#     [9, 8, 7, 6, 5, 4, 3, 2, 1],
#     [1, 2, 3, 4],
#     [4, 6, 1, 3, 7, 8, 4, 3, 4],
#     [1],
#     [1, 3, 2]
# ]


# for array in input_arrays:
#     print("")
#     print(" Input: " + str(array))
#     sorted_array = bubble_sort(array)
#     print("Output: " + str(sorted_array))
