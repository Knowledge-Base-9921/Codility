# Counting Elements / Counting Elements

# Store the data in a slightly different way

A_origin = [0,0,4,2,4,5]
A_count = [2,0,1,0,2,1] # the index corresponds to the value of A_origin, the value corresponds to the counts of the values of A_origin

'''
A_origin[0] = 0 # count of 0 is 1
A_origin[1] = 0 # count of 0 now is 2

so A_count[0] = 2

If we know that all the elements are in the set {0, 1, . . . , m}, then the array used for counting
should be of size m + 1.
'''

# O(n + m)

def counting(A,m):
    n = len(A) # O(1)
    A_count = [0] * (m+1) # O(m)

    for i in range(n): # O(n)
        A_count[A[i]]+=1 # O(1)

    return A_count

A_count_new = counting(A_origin,m=5)
print(A_count_new) 