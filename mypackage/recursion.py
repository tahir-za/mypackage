def sum_array(array):

    '''Return sum of all items in array'''
    # Check to see if array is only 1 item in  length
    if len(array)== 1:
        return array[0]
    else:
        # Return the sum of the array
        return array[0]+sum_array(array[1:])

def fibonacci(n):

    '''Return nth term in fibonacci sequence'''

    #Check input to see if it is a positive integer
    if n < 0:
        print("Please insert a positive integer")
    #First Fibonacci number is 0
    elif n == 0:
        return 0
    #Second Fibonacci number is 1
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

def factorial(n):

    '''Return n!'''
    #Check input to see if it is a positive integer
    if n < 0:
        print("Please insert a positive integer")
    else:
        # factorial 1 is 1 therefore return 1
        if n < 2:
            return 1
        # Calculate the n factorial recursively
        return n * factorial(n - 1)

def reverse(word):

    '''Return word in reverse'''

    #initalise empty string result
    result =''
    # Check input to see if it is a string or nothing
    if len(word) < 1:
        print('Please enter a word')
    else:
        #reverse word recursively
        result = word[-1] + reverse(word[:-1])
    return result
