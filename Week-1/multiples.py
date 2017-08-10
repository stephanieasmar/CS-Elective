# for loop that iterates through range of num 
# check if num % of 3 or 5 = 0, if yes, add to sum, if no, do not add to sum


# def get_multiples():
#     max = 50000000
#     sum = 0
#     i = 1
#     for i in range(1, max):
#         if (i % 3 == 0) or (i % 5 == 0):
#             sum = sum + 1
            
#     return sum

# print get_multiples()



def sum_divisible_by(number, max):
    sum = 0
    i = number
    while i < max:
        sum = sum + i
        i = i + number
    return sum


def run_program():
    MAX = 50000000
    sum = sum_divisible_by(3, MAX) + sum_divisible_by(5, MAX) - sum_divisible_by(15, MAX)
    print sum