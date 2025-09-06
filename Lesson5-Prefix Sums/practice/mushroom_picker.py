# PrefixSums / Mushroom Picker

'''
You are given a non-empty, zero-indexed array A of n (1 <= n <= 100 000) integers
a0, a1, . . . , an-1 (0 <= ai <= 1 000). This array represents number of mushrooms growing on the
consecutive spots along a road. You are also given integers k and m (0 <= k, m < n).
A mushroom picker is at spot number k on the road and should perform m moves. In
one move she moves to an adjacent spot. She collects all the mushrooms growing on spots
she visits. The goal is to calculate the maximum number of mushrooms that the mushroom
picker can collect in m moves.
For example, consider array A such that:
2 3 7 5 1 3 9
0 1 2 3 4 5 6
The mushroom picker starts at spot k = 4 and should perform m = 6 moves. She might
move to spots 3, 2, 3, 4, 5, 6 and thereby collect 1 + 5 + 7 + 3 + 9 = 25 mushrooms. This is the
maximal number of mushrooms she can collect.
'''

# O(N)

def prefix_sums(A):
    n = len(A)
    A_prefix_sum = [0] * (n+1)

    for i in range(1,n+1):
        A_prefix_sum[i] = A_prefix_sum[i-1] + A[i-1]

    return A_prefix_sum

# O(1)

def count_total(A, x, y):
    return A[y+1] - A[x]

# O(N + M)
def mushrooms(A, k, m):
    n = len(A)
    result = 0

    A_prefix = prefix_sums(A)

    # Plan: Is to make only one turn, either from L-R or R-L to optimize the solution

    # Strategy 1: Go Left and then Right
    for curr_position in range(min(m,k)+1): # m is total allowed moves, k steps are the number of steps from the left of k
        left_position = k - curr_position
        moves_remaining = m - curr_position
        potential_right_position = left_position + moves_remaining # going forward
        right_position = min(n-1, max(k, potential_right_position))

        result = max(result, count_total(A_prefix, left_position, right_position))

    # Strategy 2: Go Right and then Left
    for curr_position in range(min(m+1,n-k)):
        right_position = k + curr_position
        moves_remaining = m - curr_position
        potential_left_position = right_position - moves_remaining # going back
        left_position = max(0, min(k, potential_left_position))

        result = max(result, count_total(A_prefix, left_position, right_position))

    return result