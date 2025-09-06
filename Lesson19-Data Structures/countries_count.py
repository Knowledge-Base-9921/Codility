# Data Structures / CountBoundedSlices

# Calculate the number of slices in which (maximum - minimum <= K).

'''
An integer K and a non-empty array A consisting of N integers are given.

A pair of integers (P, Q), such that 0 ≤ P ≤ Q < N, is called a slice of array A.

A bounded slice is a slice in which the difference between the maximum and minimum values in the slice is less than or equal to K. More precisely it is a slice, such that max(A[P], A[P + 1], ..., A[Q]) − min(A[P], A[P + 1], ..., A[Q]) ≤ K.

The goal is to calculate the number of bounded slices.

For example, consider K = 2 and array A such that:

    A[0] = 3
    A[1] = 5
    A[2] = 7
    A[3] = 6
    A[4] = 3
There are exactly nine bounded slices: (0, 0), (0, 1), (1, 1), (1, 2), (1, 3), (2, 2), (2, 3), (3, 3), (4, 4).

Write a function:

def solution(K, A)

that, given an integer K and a non-empty array A of N integers, returns the number of bounded slices of array A.

If the number of bounded slices is greater than 1,000,000,000, the function should return 1,000,000,000.

For example, given:

    A[0] = 3
    A[1] = 5
    A[2] = 7
    A[3] = 6
    A[4] = 3
the function should return 9, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
K is an integer within the range [0..1,000,000,000];
each element of array A is an integer within the range [−1,000,000,000..1,000,000,000].
'''

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

from collections import deque

def solution(K, A):
    """
    Calculates the number of bounded slices in an array A.

    A slice (P, Q) is bounded if max(A[P...Q]) - min(A[P...Q]) <= K.

    Args:
        K: An integer, the maximum allowed difference between max and min in a slice.
        A: A non-empty array of N integers.

    Returns:
        The number of bounded slices. If the count exceeds 1,000,000,000,
        it returns 1,000,000,000.
    """
    N = len(A)
    count = 0
    left = 0  # Left pointer of the sliding window

    # Deques to efficiently maintain the minimum and maximum elements in the current window
    # min_deque stores indices of elements in increasing order of their values.
    # max_deque stores indices of elements in decreasing order of their values.
    min_deque = deque()
    max_deque = deque()

    # Iterate with the right pointer to expand the window
    for right in range(N):
        # Maintain min_deque: Remove elements from the right end that are greater than A[right]
        while min_deque and A[min_deque[-1]] >= A[right]:
            min_deque.pop()
        min_deque.append(right) # Add current index to min_deque

        # Maintain max_deque: Remove elements from the right end that are smaller than A[right]
        while max_deque and A[max_deque[-1]] <= A[right]:
            max_deque.pop()
        max_deque.append(right) # Add current index to max_deque

        # Shrink the window from the left if the current slice (A[left...right]) is not bounded
        # This loop ensures that A[max_deque[0]] - A[min_deque[0]] <= K always holds
        # for the current (left, right) window after the loop.
        while A[max_deque[0]] - A[min_deque[0]] > K:
            # If the element at the 'left' pointer is the current minimum in the window,
            # remove its index from the min_deque.
            if min_deque[0] == left:
                min_deque.popleft()
            # If the element at the 'left' pointer is the current maximum in the window,
            # remove its index from the max_deque.
            if max_deque[0] == left:
                max_deque.popleft()
            left += 1 # Shrink the window by moving the left pointer to the right

        # At this point, the slice A[left...right] is bounded.
        # All slices (P, right) where left <= P <= right are also bounded.
        # The number of such slices is (right - left + 1).
        count += (right - left + 1)

        # Check if the total count exceeds the maximum allowed value
        if count > 1_000_000_000:
            return 1_000_000_000

    return count