# Prime and Composite Numbers / Primality Test

'''
The primality test of n can be performed in an analogous way to counting the divisors. If we
find a number between 2 and n − 1 that divides n then n is a composite number. Otherwise,
n is a prime number.

NOTE: We assume that 1 is neither a prime nor a composite number, so the above algorithm works
only for n <= 2.
'''

# O(sqrt(n))

def primality(n):
    i = 2

    while (i*i <= n):
        if (n%i == 0):
            return False
        
        i+=1

    return False