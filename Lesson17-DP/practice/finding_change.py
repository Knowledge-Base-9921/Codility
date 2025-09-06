# Dynamic Programming / Finding Change

'''
Consider n denominations, 0 < c0 <= c1 <= . . . <= cn−1. The algorithm processes the respective
denominations and calculates the minimum number of coins needed to pay every amount
from 0 to k. When considering each successive denomination, we use the previously calculated
results for the smaller amounts.
'''

# O(NK) for both space and time

def solution1(C, k):
    n = len(C)
    INF = float('inf')

    dp = [[0] * (k + 1) for _ in range(n + 1)]
    dp[0][0] = 0
    for j in range(1, k + 1):
        dp[0][j] = INF

    for i in range(1, n + 1):
        current_coin_value = C[i - 1]

        # Inner loop iterates through all possible amounts 'j' from 0 to k.
        for j in range(k + 1):
            # Option 1: Don't use the current coin (C[i-1]).
            cost_without_current_coin = dp[i - 1][j]

            # Option 2: Use the current coin (C[i-1]).
            cost_with_current_coin = INF # Initialize to infinity

            if j >= current_coin_value:
                if dp[i][j - current_coin_value] != INF:
                    cost_with_current_coin = dp[i][j - current_coin_value] + 1
            
            # Take the minimum of the two options.
            dp[i][j] = min(cost_without_current_coin, cost_with_current_coin)

    # The final answer is the value at dp[n][k], which represents
    return dp[n][k]

# O(NK) but space is only O(K)

def solution2(C, k):
    n = len(C)
    INF = float('inf')

    dp = [0] + INF * k

    for i in range(1, n+1):
        for j in range(C[i-1], k+1):
            dp[j] = min(dp[j - C[i-1]] + 1, dp[j])

    return dp