# Sorting / Selection Sort

'''
Find the minimal element and swap it with the first element of an array. Next,
just sort the rest of the array, without the first element, in the same way.
Notice that after k iterations (repetition of everything inside the loop) the first k elements
will be sorted in the right order (this type of a property is called the loop invariant).
'''

# O(n^2)

def selection_sort(A):
    n = len(A)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if A[j] < A[min_idx]:
                min_idx = j
        A[i], A[min_idx] = A[min_idx], A[i]


    return A 
