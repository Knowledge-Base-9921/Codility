# Iterations / Factorial of a number

'''
We are given some positive integer n. Let’s compute the factorial of n and assign
it to the variable factorial. The factorial of n is n! = 1 · 2 · . . . · n. We can obtain it by
starting with 1 and multiplying it by all the integers from 1 to n.
'''

n = int(input("Enter n: "))
result = 1
for i in range(2,n+1):
    result *= i

print(f"Factorial of {n} is {result}")