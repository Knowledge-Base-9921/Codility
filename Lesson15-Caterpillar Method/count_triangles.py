# Caterpillar Method / CountTriangles

# Count the number of triangles that can be built from a given set of edges.

'''
An array A consisting of N integers is given. A triplet (P, Q, R) is triangular if it is possible to build a triangle with sides of lengths A[P], A[Q] and A[R]. In other words, triplet (P, Q, R) is triangular if 0 ≤ P < Q < R < N and:

A[P] + A[Q] > A[R],
A[Q] + A[R] > A[P],
A[R] + A[P] > A[Q].
For example, consider array A such that:

  A[0] = 10    A[1] = 2    A[2] = 5
  A[3] = 1     A[4] = 8    A[5] = 12
There are four triangular triplets that can be constructed from elements of this array, namely (0, 2, 4), (0, 2, 5), (0, 4, 5), and (2, 4, 5).

Write a function:

def solution(A)

that, given an array A consisting of N integers, returns the number of triangular triplets in this array.

For example, given array A such that:

  A[0] = 10    A[1] = 2    A[2] = 5
  A[3] = 1     A[4] = 8    A[5] = 12
the function should return 4, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..1,000];
each element of array A is an integer within the range [1..1,000,000,000].
'''

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Implement your solution here
    n = len(A)
    
    # A triangle requires at least 3 edges.
    if n < 3:
        return 0

    # Step 1: Sort the array.
    # Sorting is crucial for efficiency. If A[P] <= A[Q] <= A[R],
    # then two conditions (A[Q] + A[R] > A[P] and A[R] + A[P] > A[Q])
    # are automatically satisfied. We only need to check A[P] + A[Q] > A[R].
    A.sort()

    # Initialize the count of triangular triplets.
    triangle_count = 0

    # Step 2: Iterate through all possible triplets (P, Q, R).
    # We fix P and Q, and then efficiently find valid R values.
    # P will iterate from the first element up to the third-to-last element.
    for P in range(n - 2):
        # Q will iterate from the element after P up to the second-to-last element.
        # R_pointer will start from the element after Q.
        R_pointer = P + 2 
        
        for Q in range(P + 1, n - 1):
            # For fixed A[P] and A[Q], we need to find all A[R] such that A[P] + A[Q] > A[R].
            # Since the array A is sorted, we can efficiently move the R_pointer.
            # While R_pointer is within bounds and A[P] + A[Q] is greater than A[R_pointer]:
            # This means A[R_pointer] can form a triangle with A[P] and A[Q].
            # All elements from A[R_pointer] up to the current R_pointer - 1 are also valid.
            while R_pointer < n and A[P] + A[Q] > A[R_pointer]:
                R_pointer += 1
            
            # At this point, R_pointer is either out of bounds, or A[P] + A[Q] <= A[R_pointer].
            # All elements from index Q + 1 up to R_pointer - 1 can form a triangle with A[P] and A[Q].
            # The number of such elements is (R_pointer - 1) - (Q + 1) + 1, which simplifies to R_pointer - (Q + 1).
            # We add this count to our total.
            triangle_count += (R_pointer - (Q + 1))

    return triangle_count