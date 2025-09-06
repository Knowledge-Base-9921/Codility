# Time Complexity / Comparison of different time complexities

## O(1)

def constant(n):
    result = n * n
    return result

## O(log(n))

def logarithmic(n):
    result = 0
    while n > 1:
        n //=2 # value of n is halved every iteration
        result += 1
    return result

## O(n)

def linear(n):
    for i in range(n): # this is O(n)
        print(i) # this is O(1)

## O(n+m)

def linear2(n,m):
    for i in range(n):
        print(i)

    for i in range(m):
        print(i)

## O(n^2)

def quadratic(n):
    for i in range(n):
        for j in range(i,n):
            print(j)
