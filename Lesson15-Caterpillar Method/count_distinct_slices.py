# Caterpillar Method / CountDistinctSlices

# Count the number of distinct slices (containing only unique numbers).

'''
An integer M and a non-empty array A consisting of N non-negative integers are given. All integers in array A are less than or equal to M.

A pair of integers (P, Q), such that 0 ≤ P ≤ Q < N, is called a slice of array A. The slice consists of the elements A[P], A[P + 1], ..., A[Q]. A distinct slice is a slice consisting of only unique numbers. That is, no individual number occurs more than once in the slice.

For example, consider integer M = 6 and array A such that:

    A[0] = 3
    A[1] = 4
    A[2] = 5
    A[3] = 5
    A[4] = 2
There are exactly nine distinct slices: (0, 0), (0, 1), (0, 2), (1, 1), (1, 2), (2, 2), (3, 3), (3, 4) and (4, 4).

The goal is to calculate the number of distinct slices.

Write a function:

def solution(M, A)

that, given an integer M and a non-empty array A consisting of N integers, returns the number of distinct slices.

If the number of distinct slices is greater than 1,000,000,000, the function should return 1,000,000,000.

For example, given integer M = 6 and array A such that:

    A[0] = 3
    A[1] = 4
    A[2] = 5
    A[3] = 5
    A[4] = 2
the function should return 9, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
M is an integer within the range [0..100,000];
each element of array A is an integer within the range [0..M].
'''

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(M, A):
    # Implement your solution here
    n = len(A)
    
    # Handle empty array case
    if n == 0:
        return 0

    # `last_seen[x]` will store the last index where value `x` was seen.
    # Initialize with -1, indicating not seen yet.
    # Size M+1 to accommodate values from 0 to M.
    last_seen = [-1] * (M + 1)

    # `left` pointer of the sliding window.
    left = 0
    # `count` stores the total number of distinct slices.
    total_distinct_slices = 0
    
    # The problem states the result should be capped at 1,000,000,000.
    MAX_RESULT = 1_000_000_000

    # Iterate with the `right` pointer to expand the window.
    for right in range(n):
        current_element = A[right]

        # If the current element `A[right]` has been seen before within the current window
        # (i.e., its `last_seen` index is greater than or equal to `left`),
        # then we need to move the `left` pointer to the right of the previous occurrence
        # of `current_element` to make the window distinct again.
        if last_seen[current_element] >= left:
            left = last_seen[current_element] + 1
        
        # Update the last seen index for the current element.
        last_seen[current_element] = right

        # The number of distinct slices ending at `right` is `(right - left + 1)`.
        # For example, if the distinct window is [x, y, z] and `right` is at `z`,
        # then slices ending at `z` are [z], [y,z], [x,y,z]. The count is 3.
        # This is (right - left + 1).
        total_distinct_slices += (right - left + 1)

        # Cap the result at 1,000,000,000 as per problem requirements.
        if total_distinct_slices > MAX_RESULT:
            return MAX_RESULT

    return total_distinct_slices
