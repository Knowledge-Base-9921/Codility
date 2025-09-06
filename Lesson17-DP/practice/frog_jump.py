# Dynamic Programming / Frog Jump

'''
A small frog wants to get from position 0 to k (1 <= k <= 10 000). The frog can
jump over any one of n fixed distances s0, s1, . . . , sn−1 (1 <= si <= k). The goal is to count the
number of different ways in which the frog can jump to position k. To avoid overflow, it is
sufficient to return the result modulo q, where q is a given number.
We assume that two patterns of jumps are different if, in one pattern, the frog visits
a position which is not visited in the other pattern.
'''

# O(NK) Time, O(K) Space

def frog(S, k, q):
    n = len(S)
    dp = [1] + [0] * k

    for j in range(1, k+1):
        for i in range(n):
            if S[i] <= j:
                dp[j] = (dp[j] + dp[j - S[i]]) % q

    return dp[k]