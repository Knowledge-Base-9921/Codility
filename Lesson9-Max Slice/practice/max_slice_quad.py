# Maximal Slice Problem / Maximal Slice Quadratic

'''
Let’s define a problem relating to maximum slices. You are given a sequence of n integers
a0, a1, . . . , an−1 and the task is to find the slice with the largest sum. More precisely, we are
looking for two indices p, q such that the total ap + ap+1 + . . . + aq is maximal. We assume
that the slice can be empty and its sum equals 0.
a0 a1 a2 a3 a4 a5 a6
5 -7 3 5 -2 4 -1
In the picture, the slice with the largest sum is highlighted in gray. The sum of this slice
equals 10 and there is no slice with a larger sum. Notice that the slice we are looking for may
contain negative integers, as shown above.
'''

# O(n)

def prefix_sums(A):
    n = len(A)
    A_prefix_sum = [0] * (n+1)

    for i in range(1,n+1):
        A_prefix_sum[i] = A_prefix_sum[i-1] + A[i-1]

    return A_prefix_sum

# O(N^2) -- Way 1

def quadratic_max_slice(A):
    n = len(A)
    result = 0

    A_prefix = prefix_sums(A)

    for i in range(n):
        for j in range(i,n):
            _sum = A_prefix[j+1] - A_prefix[i]
            result = max(result, _sum)
    return result

# O(N^2) -- Way 2

def quadratic_max_slice2(A):
    n = len(A)
    result = 0

    for i in range(n):
        _sum = 0
        for j in range(i,n):
            _sum += A[j]
            result = max(result, _sum)
    return result