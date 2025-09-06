# Sorting / Counting Sort

'''
First, count the elements in the array of counters (see chapter 2). Next, just iterate
through the array of counters in increasing order.
Notice that we have to know the range of the sorted values. If all the elements are in the
set {0, 1, . . . , k}, then the array used for counting should be of size k + 1. The limitation here
may be available memory.
'''

# O(n + m)

def counting(A,m):
    n = len(A) # O(1)
    A_count = [0] * (m+1) # O(m)

    for i in range(n): # O(n)
        A_count[A[i]]+=1 # O(1)

    return A_count

# O(n + k)

def counting_sort(A, k):
    A_count = counting(A, k)

    _left = 0
    for i in range(k+1):
        for _ in range(A_count[i]):
            A[_left] = i
            _left += 1
    
    return A