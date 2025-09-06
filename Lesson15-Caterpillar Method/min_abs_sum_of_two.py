# Caterpillar Method / MinAbsSumOfTwo

# Find the minimal absolute value of a sum of two elements.

'''
Let A be a non-empty array consisting of N integers.

The abs sum of two for a pair of indices (P, Q) is the absolute value |A[P] + A[Q]|, for 0 ≤ P ≤ Q < N.

For example, the following array A:

  A[0] =  1
  A[1] =  4
  A[2] = -3
has pairs of indices (0, 0), (0, 1), (0, 2), (1, 1), (1, 2), (2, 2).
The abs sum of two for the pair (0, 0) is A[0] + A[0] = |1 + 1| = 2.
The abs sum of two for the pair (0, 1) is A[0] + A[1] = |1 + 4| = 5.
The abs sum of two for the pair (0, 2) is A[0] + A[2] = |1 + (−3)| = 2.
The abs sum of two for the pair (1, 1) is A[1] + A[1] = |4 + 4| = 8.
The abs sum of two for the pair (1, 2) is A[1] + A[2] = |4 + (−3)| = 1.
The abs sum of two for the pair (2, 2) is A[2] + A[2] = |(−3) + (−3)| = 6.

Write a function:

def solution(A)

that, given a non-empty array A consisting of N integers, returns the minimal abs sum of two for any pair of indices in this array.

For example, given the following array A:

  A[0] =  1
  A[1] =  4
  A[2] = -3
the function should return 1, as explained above.

Given array A:

  A[0] = -8
  A[1] =  4
  A[2] =  5
  A[3] =-10
  A[4] =  3
the function should return |(−8) + 5| = 3.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000,000..1,000,000,000].
'''

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Implement your solution here

    n = len(A)
    
    if n == 0:
        return 0

    # Step 1: Sort the array.
    # Sorting is crucial for the two-pointer approach to work efficiently.
    # It allows us to systematically move pointers to find the smallest absolute sum.
    A.sort()

    # Initialize two pointers: 'left' at the beginning and 'right' at the end.
    left = 0
    right = n - 1

    # Initialize 'min_abs_sum' to a very large value.
    # This ensures that any valid sum found will be smaller.
    # The maximum possible sum is 2 * 1,000,000,000, so float('inf') is appropriate.
    min_abs_sum = float('inf')

    # Step 2: Use a two-pointer approach to find the minimal absolute sum.
    # The loop continues as long as the left pointer is less than or equal to the right pointer.
    while left <= right:
        # Calculate the current sum of elements pointed to by left and right.
        current_sum = A[left] + A[right]

        # Update the minimum absolute sum found so far.
        min_abs_sum = min(min_abs_sum, abs(current_sum))

        # Optimization: If the current sum is 0, we've found the absolute minimum.
        # No other sum can be smaller in absolute value.
        if current_sum == 0:
            return 0

        # Move pointers based on the current sum:
        # If current_sum is negative, it means A[left] is too small (too negative)
        # or A[right] is not large enough (positive).
        # To make the sum closer to zero (or positive), we need to increase A[left].
        if current_sum < 0:
            left += 1
        # If current_sum is positive, it means A[right] is too large (too positive)
        # or A[left] is not small enough (negative).
        # To make the sum closer to zero (or negative), we need to decrease A[right].
        else: # current_sum > 0
            right -= 1

    return min_abs_sum