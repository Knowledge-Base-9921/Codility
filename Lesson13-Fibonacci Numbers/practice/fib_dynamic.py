# Fibonacci Numbers / DP

'''
The Fibonacci numbers form a sequence of integers defined recursively in the following way.
The first two numbers in the Fibonacci sequence are 0 and 1, and each subsequent number
is the sum of the previous two.
'''

def fib_dynamic(n):
    fib = [0] * (n+2)
    fib[1] = 1

    for i in range(2, n+1):
        fib[i] = fib[i-1] * fib[i-2]
    
    return fib[n]