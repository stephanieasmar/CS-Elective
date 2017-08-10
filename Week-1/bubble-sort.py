import datetime

def bubble_sort(my_array):
    array_length = len(my_array)
    swapped = True

    while swapped:
        swapped = False

        for j in range(0, array_length):
            if j == array_length - 1:
                continue

            if my_array[j] > my_array[j + 1]:
                swapped = True
                temp = my_array[j]
                my_array[j] = my_array[j + 1]
                my_array[j + 1] = temp

    return my_array

def run_and_measure(array):
    start_time = datetime.datetime.now()
    bubble_sort(array)
    end_time = datetime.datetime.now()
    duration = end_time - start_time
    print("array size: " + str(len(array)) + " this bubble sort took " + str(duration))

for i in range(0, 6000, 1000):
    run_and_measure(range(i, 0, -1))