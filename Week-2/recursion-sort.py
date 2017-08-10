def example_one(i):
    if i == 10:
        return

    print(i)
    i = i + 1
    example_one(i)

# example_one(0)


def fibonacci(x, y, max, counter=0):
    if counter == max:
        return

    print(counter)
    counter += 1
    next_num = x + y
    print(x)
    fibonacci(y, next_num, max, counter)


# fibonacci(1, 1, 10) #calls fib function



#prints a star pyramid
def stars(max, counter=0):
    if counter == max:
        return
    
    counter += 1
    print(counter * "*")
    stars(max, counter)

# stars(20)

#the below function returns the factorial of all numbers up until the number(n) that is passed...
def factorial(n):
    if n == 1 or n == 0: #there is no factorial of 1 or 0, so we have to account for this base case here...
        return 1
    
    fact_num = n * factorial(n-1) #define a new variable that is equal to the number passed(n) times factorial of n minus 1 (ex: n=5, n-1=4)...
    print(str(n) + '! = ' + str(fact_num)) #print n! = new variable (fact_num)
    return fact_num #return new variable...

factorial(10) #Dont forget to call the function!!!


#How to reverse and array with a for loop:
array = [1, 2, 3, 4, 5]
for i in range(len(array) / 2)
    j = len(array) - i - 1
    array[i], array[len(array) - 1 - i] = array[len(array) - 1 - i], array[i]


#How to reverse an array with recursion:
def rev_array(array, i):
    if i >= len(array) / 2 or len(array) == none:
        return array

        j = len(array) - i - 1
        array[i], array[j] = array[j], array[i]
        return reverse_array(array, i + 1)

    

    
    
    



    

























