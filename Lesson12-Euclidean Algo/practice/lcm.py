# Euclidean Algorithm / Least Common Multiple

# O(log(a+b))

def gcd(a, b):
    if a%b == 0:
        return b
    
    return gcd(b, a%b)

# O(log(a+b))

def lcm(a,b):
    return (a*b) / gcd(a,b)