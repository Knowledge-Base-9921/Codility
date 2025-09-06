# Sieve of Eratosthenes / Factorization

'''
Factorization is the process of decomposition into prime factors. More precisely, for a given
number x we want to find primes p1, p2, . . . , pk whose product equals x.
Use of the sieve enables fast factorization. Let’s modify the sieve algorithm slightly. For
every crossed number we will remember the smallest prime that divides this number.
'''

def factorization(n):
    _fact = [0] * (n+1)
    i = 2

    while(i*i <= n):
        if(_fact[i] == 0):
            k = i*i
            while(k<=n):
                if(_fact[k] == 0):
                    _fact[k] = i
                k += i
        i+=1
    
    return _fact

# O(logX)

def factorization_of_x(x, F):
    prime_factors = []
    while(F[x] > 0):
        prime_factors += [F[x]]
        x /= F[x]

    prime_factors += [x]

    return prime_factors