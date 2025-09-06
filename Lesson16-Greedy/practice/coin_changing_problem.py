# Greedy Algorithm / Coin Changing Problem

'''
For a given set of denominations, you are asked to find the minimum number of coins with
which a given amount of money can be paid. That problem can be approached by a greedy
algorithm that always selects the largest denomination not exceeding the remaining amount
of money to be paid. As long as the remaining amount is greater than zero, the process is
repeated.
A correct algorithm should always return the minimum number of coins. It turns out
that the greedy algorithm is correct for only some denomination selections, but not for all.
For example, for coins of values 1, 2 and 5 the algorithm returns the optimal number of
coins for each amount of money, but for coins of values 1, 3 and 4 the algorithm may return
a suboptimal result. An amount of 6 will be paid with three coins: 4, 1 and 1 by using the
greedy algorithm. The optimal number of coins is actually only two: 3 and 3.
Consider n denominations 0 < m0 <= m1 <= . . . <= mn−1 and the amount k to be paid.
'''

def greedyCoinChanging(M, k):
    """
    Implements a greedy algorithm to find the minimum number of coins
    to make change for a given amount 'k', using a set of denominations 'M'.

    This greedy approach works correctly for 'canonical' coin systems
    (e.g., standard currency denominations like [1, 5, 10, 25]).
    It may not yield the optimal solution for all arbitrary coin systems.

    Args:
        M: A list of coin denominations, assumed to be sorted in ascending order.
           Example: [1, 5, 10, 25]
        k: The target amount for which to make change.

    Returns:
        A list of tuples, where each tuple is (denomination, count),
        representing the number of coins of each denomination used.
        The list is ordered from largest to smallest denomination.
    """
    n = len(M)
    result = [] # Initialize an empty list to store the coin counts

    # Iterate through the coin denominations from largest to smallest.
    # This is crucial for the greedy strategy.
    # range(start, stop, step):
    # n - 1: Start from the index of the largest denomination.
    # -1: Stop before index -1 (i.e., include index 0).
    # -1: Step backwards (decrement index by 1).
    for i in range(n - 1, -1, -1):
        current_denomination = M[i]

        # Calculate how many coins of the current denomination can be used.
        # Integer division (//) gives the maximum whole number of coins.
        count = k // current_denomination
        
        # Add the (denomination, count) pair to the result list.
        # This records how many coins of the current denomination are taken.
        result.append((current_denomination, count))
        
        # Update the remaining amount 'k'.
        # The modulo operator (%) calculates the remainder after taking 'count' coins
        # of the current denomination. This remainder is what needs to be made up
        # by smaller denominations.
        k %= current_denomination
        
        # Optimization: If the remaining amount 'k' becomes 0,
        # we have successfully made change, so we can stop early.
        if k == 0:
            break

    return result