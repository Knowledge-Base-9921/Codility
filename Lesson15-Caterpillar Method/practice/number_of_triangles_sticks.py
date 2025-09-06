# Caterpillar Method / Number of triangles created from sticks

'''
You are given n sticks (of lengths 1 <= a0 <= a1 <= . . . <= an−1 <= 109). The goal is
to count the number of triangles that can be constructed using these sticks. More precisely,
we have to count the number of triplets at indices x < y < z, such that ax + ay > az.
'''

# O(N)

def triangle(A):
    n = len(A)
    result = 0

    for x in range(n):
        z = x + 2

        for y in range(x+1, n):
            while (z < n) and (A[x] + A[y] > A[z]):
                z += 1
            result += (z - y - 1)

    
    return result