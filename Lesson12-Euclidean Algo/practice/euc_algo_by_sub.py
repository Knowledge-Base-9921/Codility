# Euclidean Algorithm / Euclidean algorithm by subtraction

#  Greatest common divisor by subtraction.

'''
The original version of Euclid’s algorithm is based on subtraction: we recursively subtract
the smaller number from the larger.
'''

def gcd(a, b):
    if a==b:
        return a
    
    if a>b:
        gcd(a-b,b)
    else:
        gcd(a, b-a)