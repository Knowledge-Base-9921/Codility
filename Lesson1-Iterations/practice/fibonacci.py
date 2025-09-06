# Iterations / Fibonacci Sequence

'''
The Fibonacci numbers4 form a sequence of integers defined recursively in the
following way. The first two numbers in the Fibonacci sequence are 0 and 1, and each subsequent number is the sum of the previous two. The first few elements in this sequence are: 0,
1, 1, 2, 3, 5, 8, 13. Let’s write a program that prints all the Fibonacci numbers, not exceeding
a given integer n
'''

n = int(input("Enter n: "))

result = 0 # 0 1 1 2 3 5 8 13

_previous = 0
_next = 1

while _previous <= n: # the condition is to not exceed a given integer n, else for loop would also work
    print(_previous)
    _sum = _previous + _next
    _previous = _next
    _next = _sum