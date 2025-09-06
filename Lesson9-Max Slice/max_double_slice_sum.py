# Maximum Slice Problem / Max Double Slice Sum

# Find the maximal sum of any double slice.

'''
A non-empty array A consisting of N integers is given.

A triplet (X, Y, Z), such that 0 ≤ X < Y < Z < N, is called a double slice.

The sum of double slice (X, Y, Z) is the total of A[X + 1] + A[X + 2] + ... + A[Y − 1] + A[Y + 1] + A[Y + 2] + ... + A[Z − 1].

For example, array A such that:

    A[0] = 3
    A[1] = 2
    A[2] = 6
    A[3] = -1
    A[4] = 4
    A[5] = 5
    A[6] = -1
    A[7] = 2
contains the following example double slices:

double slice (0, 3, 6), sum is 2 + 6 + 4 + 5 = 17,
double slice (0, 3, 7), sum is 2 + 6 + 4 + 5 − 1 = 16,
double slice (3, 4, 5), sum is 0.
The goal is to find the maximal sum of any double slice.

Write a function:

def solution(A)

that, given a non-empty array A consisting of N integers, returns the maximal sum of any double slice.

For example, given:

    A[0] = 3
    A[1] = 2
    A[2] = 6
    A[3] = -1
    A[4] = 4
    A[5] = 5
    A[6] = -1
    A[7] = 2
the function should return 17, because no double slice of array A has a sum of greater than 17.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [3..100,000];
each element of array A is an integer within the range [−10,000..10,000].
'''

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Implement your solution here
    n = len(A)

    # A double slice (X, Y, Z) requires at least 4 elements (0, 1, 2, 3) for X=0, Y=1, Z=3.
    # If N < 3, no valid X, Y, Z indices exist.
    # If N = 3, X=0, Y=1, Z=2, the sum would be empty.
    # So, if N <= 3, it's impossible to form a double slice with elements in between.
    if n <= 3:
        return 0

    # dp_forward[i] stores the maximum sum of a contiguous subarray ending at index i,
    # considering only elements from A[1] up to A[i].
    # We initialize with 0s because a negative sum contributes nothing (or makes it worse)
    # to a double slice, so we can effectively "start over" with 0.
    dp_forward = [0] * n
    for i in range(1, n - 1): # Iterate from A[1] to A[N-2]
        # The sum ending at 'i' is either A[i] itself, or A[i] plus the max sum ending at 'i-1'.
        # We take max(0, ...) because we don't want negative sums to propagate and reduce future sums.
        dp_forward[i] = max(0, dp_forward[i-1] + A[i])

    # dp_backward[i] stores the maximum sum of a contiguous subarray starting at index i,
    # considering only elements from A[i] down to A[N-2].
    # We initialize with 0s for the same reason as dp_forward.
    dp_backward = [0] * n
    for i in range(n - 2, 0, -1): # Iterate from A[N-2] down to A[1]
        # The sum starting at 'i' is either A[i] itself, or A[i] plus the max sum starting at 'i+1'.
        # We take max(0, ...) to avoid propagating negative sums.
        dp_backward[i] = max(0, dp_backward[i+1] + A[i])

    # Now, iterate through all possible 'Y' values to find the maximum double slice sum.
    # Y can range from 1 to N-2 (exclusive of A[0] and A[N-1]).
    # For a double slice (X, Y, Z), Y is the excluded middle element.
    # The sum is (max sum ending at Y-1) + (max sum starting at Y+1).
    max_double_slice_sum = 0
    for y in range(1, n - 1): # Y can be from index 1 to n-2 (inclusive)
        # The sum for a double slice with middle element A[y] is:
        # (max sum of elements from X+1 to Y-1) + (max sum of elements from Y+1 to Z-1)
        # dp_forward[y-1] gives the max sum ending at y-1 (which is the first part of the slice)
        # dp_backward[y+1] gives the max sum starting at y+1 (which is the second part of the slice)
        current_double_slice_sum = dp_forward[y-1] + dp_backward[y+1]
        
        # Update the overall maximum double slice sum found so far.
        max_double_slice_sum = max(max_double_slice_sum, current_double_slice_sum)

    return max_double_slice_sum
