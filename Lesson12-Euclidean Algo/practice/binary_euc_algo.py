# Euclidean Algorithm / Binary Euclidean algorithm

'''
This algorithm finds the gcd using only subtraction, binary representation, shifting and parity
testing. We will use a divide and conquer technique.
The following function calculate gcd(a, b, res) = gcd(a, b, 1) · res. So to calculate
gcd(a, b) it suffices to call gcd(a, b, 1) = gcd(a, b).
'''

def gcd(a, b, res):
    if a==b:
        return res * a
    elif (a%2 == 0) and (b%2 == 0):
        return gcd(a // 2, b // 2, 2 * res)
    elif (a%2 == 0):
        return gcd(a // 2, b, res)
    elif (b%2 == 0):
        return gcd(a, b//2, res)
    elif a>b:
        return gcd(a-b, b, res)
    
    return gcd(a,b-a, res)