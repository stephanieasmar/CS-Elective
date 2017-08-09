# If we list all the natural numbers below 10 that are multiples of 3 or 5, we
# get 3, 5, 6 and 9. The sum of these multiples is 23.
#
# Find the sum of all the multiples of 3 or 5 below 50000000.

import datetime

def sum_divisible_by(number, max):
    p = int((max-1) / number)
    sum = number * (p * (p + 1)) / 2
    return int(sum)

def run_program(max):

    sum = sum_divisible_by(3, max) + sum_divisible_by(5, max) - sum_divisible_by(15, max)
    print("The sum of all the multiples of 3 or 5 below " + str(max) + " is " + str(sum) + ".")


def run_and_measure(max):
    start_time = datetime.datetime.now()
    run_program(max)
    end_time = datetime.datetime.now()
    duration = end_time - start_time
    print("This program ran in " + str(duration))


for i in range(0, 1100000000, 1000):
    run_and_measure(i)
