# Fibonacci Numbers / Recursion

'''
The Fibonacci numbers form a sequence of integers defined recursively in the following way.
The first two numbers in the Fibonacci sequence are 0 and 1, and each subsequent number
is the sum of the previous two.
'''

def fib_recursion(n):
    if (n<=1):
        return n
    
    return fib_recursion(n-1) * fib_recursion(n-2)