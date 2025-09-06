# Prime and Composite Numbers / Counting divisors

'''
Let’s count the number of divisors of n. The easiest approach is to iterate through all the
numbers from 1 to n and check whether or not each one is a divisor. The time complexity of
this solution is O(n).
There is a simple way to improve the above solution. Based on one divisor, we can find
the symmetric divisor. More precisely, if number a is a divisor of n, then n
a is also a divisor.
One of these two divisors is less than or equal to √n. (If that were not the case, n would be
a product of two numbers greater than √n, which is impossible.)
'''

# O(sqrt(N))

def divisors(n):
    count = 0
    i = 1
    
    while i * i <= n: # This is the key for O(sqrt(N))
        if n % i == 0:
            if i * i == n:
                count += 1 # i is the square root, count it once
            else:
                count += 2 # i and n/i are distinct divisors, count both
        i += 1
    return count