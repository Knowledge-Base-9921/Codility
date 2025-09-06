# Dynamic Programming / MinAbsSum

# Given array of integers, find the lowest absolute sum of elements.

'''
For a given array A of N integers and a sequence S of N integers from the set {−1, 1}, we define val(A, S) as follows:

val(A, S) = |sum{ A[i]*S[i] for i = 0..N−1 }|

(Assume that the sum of zero elements equals zero.)

For a given array A, we are looking for such a sequence S that minimizes val(A,S).

Write a function:

def solution(A)

that, given an array A of N integers, computes the minimum value of val(A,S) from all possible values of val(A,S) for all possible sequences S of N integers from the set {−1, 1}.

For example, given array:

  A[0] =  1
  A[1] =  5
  A[2] =  2
  A[3] = -2
your function should return 0, since for S = [−1, 1, −1, 1], val(A, S) = 0, which is the minimum possible value.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..20,000];
each element of array A is an integer within the range [−100..100].
'''

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    if not A:
        return 0
    if len(A) == 1:
        return abs(A[0])

    A = [abs(x) for x in A]
    total_sum = sum(A)
    max_val = max(A)

    # Frequency count of each absolute value
    count = [0] * (max_val + 1)
    for num in A:
        count[num] += 1

    # Initialize DP array
    dp = [-1] * (total_sum + 1)
    dp[0] = 0

    # Bounded Knapsack DP using frequency count
    for val in range(1, max_val + 1):
        if count[val] > 0:
            for s in range(total_sum + 1):
                if dp[s] >= 0:
                    dp[s] = count[val]
                elif s >= val and dp[s - val] > 0:
                    dp[s] = dp[s - val] - 1

    # Find minimum absolute difference
    result = total_sum
    for i in range(total_sum // 2 + 1):
        if dp[i] >= 0:
            result = min(result, total_sum - 2 * i)

    return result
