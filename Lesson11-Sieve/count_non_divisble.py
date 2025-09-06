# Sieve of Eratosthenes / Count Non Divisible

# Calculate the number of elements of an array that are not divisors of each element.

'''
You are given an array A consisting of N integers.

For each number A[i] such that 0 ≤ i < N, we want to count the number of elements of the array that are not the divisors of A[i]. We say that these elements are non-divisors.

For example, consider integer N = 5 and array A such that:

    A[0] = 3
    A[1] = 1
    A[2] = 2
    A[3] = 3
    A[4] = 6
For the following elements:

A[0] = 3, the non-divisors are: 2, 6,
A[1] = 1, the non-divisors are: 3, 2, 3, 6,
A[2] = 2, the non-divisors are: 3, 3, 6,
A[3] = 3, the non-divisors are: 2, 6,
A[4] = 6, there aren't any non-divisors.
Write a function:

def solution(A)

that, given an array A consisting of N integers, returns a sequence of integers representing the amount of non-divisors.

Result array should be returned as an array of integers.

For example, given:

    A[0] = 3
    A[1] = 1
    A[2] = 2
    A[3] = 3
    A[4] = 6
the function should return [2, 4, 3, 2, 0], as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..50,000];
each element of array A is an integer within the range [1..2 * N].
'''

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Implement your solution here
    n = len(A)

    # Find the maximum value in A. This helps to define the size of auxiliary arrays.
    # The problem constraints state elements are up to 2 * N.
    max_val = 0
    if n > 0:
        max_val = max(A)
    else:
        return [] # Return empty list for empty input array

    # Step 1: Count frequencies of each number in A.
    # `counts[x]` will store how many times `x` appears in `A`.
    # Array size is `max_val + 1` to accommodate values up to `max_val`.
    counts = [0] * (max_val + 1)
    for x in A:
        counts[x] += 1

    # Step 2: Precompute for each number `x` (from 1 to max_val),
    # how many elements in the original array A are divisors of `x`.
    # `num_divisors_of_x_in_A[x]` will store this count.
    num_divisors_of_x_in_A = [0] * (max_val + 1)

    # Iterate through all possible divisors `d` from 1 up to `max_val`.
    for d in range(1, max_val + 1):
        # Iterate through all multiples `m` of `d` up to `max_val`.
        # If a multiple `m` is present in the array A (i.e., `counts[m] > 0`),
        # then `d` is a divisor of `m`.
        # We add the frequency of `m` to `num_divisors_of_x_in_A[m]`.
        # This way, `num_divisors_of_x_in_A[m]` accumulates the sum of frequencies
        # of all its divisors that are present in A.
        for m in range(d, max_val + 1, d):
            if counts[m] > 0:
                num_divisors_of_x_in_A[m] += counts[d] # Add count of divisor 'd' to its multiple 'm'

    # Step 3: Calculate the number of non-divisors for each element in the original array A.
    result = [0] * n
    for i in range(n):
        element = A[i]
        # Total elements in A is `n`.
        # Number of divisors of `element` (that are also in A) is `num_divisors_of_x_in_A[element]`.
        # The number of non-divisors is total elements minus number of divisors.
        result[i] = n - num_divisors_of_x_in_A[element]

    return result