# Maximum Slice Problem / Max Slice Sum

# Find a maximum sum of a compact subsequence of array elements.

'''
A non-empty array A consisting of N integers is given. A pair of integers (P, Q), such that 0 ≤ P ≤ Q < N, is called a slice of array A. The sum of a slice (P, Q) is the total of A[P] + A[P+1] + ... + A[Q].

Write a function:

def solution(A)

that, given an array A consisting of N integers, returns the maximum sum of any slice of A.

For example, given array A such that:

A[0] = 3  A[1] = 2  A[2] = -6
A[3] = 4  A[4] = 0
the function should return 5 because:

(3, 4) is a slice of A that has sum 4,
(2, 2) is a slice of A that has sum −6,
(0, 1) is a slice of A that has sum 5,
no other slice of A has sum greater than (0, 1).
Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..1,000,000];
each element of array A is an integer within the range [−1,000,000..1,000,000];
the result will be an integer within the range [−2,147,483,648..2,147,483,647].
'''

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Implement your solution here
    n = len(A)

    # Handle empty array case
    if n == 0:
        return 0

    # Initialize current_max and global_max
    # We initialize both with the first element of the array.
    # This correctly handles cases with all negative numbers.
    current_max = A[0]
    global_max = A[0]

    # Iterate through the array starting from the second element
    for i in range(1, n):
        # For each element, decide whether to extend the previous subarray
        # or start a new subarray from the current element.
        current_max = max(A[i], current_max + A[i])
        
        # Update the overall maximum sum found so far.
        global_max = max(global_max, current_max)

    return global_max