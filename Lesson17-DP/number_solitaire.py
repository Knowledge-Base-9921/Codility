# Dynamic Programming / Number Solitaire

# In a given array, find the subset of maximal sum in which the distance between consecutive elements is at most 6.

'''
A game for one player is played on a board consisting of N consecutive squares, numbered from 0 to N − 1. There is a number written on each square. A non-empty array A of N integers contains the numbers written on the squares. Moreover, some squares can be marked during the game.

At the beginning of the game, there is a pebble on square number 0 and this is the only square on the board which is marked. The goal of the game is to move the pebble to square number N − 1.

During each turn we throw a six-sided die, with numbers from 1 to 6 on its faces, and consider the number K, which shows on the upper face after the die comes to rest. Then we move the pebble standing on square number I to square number I + K, providing that square number I + K exists. If square number I + K does not exist, we throw the die again until we obtain a valid move. Finally, we mark square number I + K.

After the game finishes (when the pebble is standing on square number N − 1), we calculate the result. The result of the game is the sum of the numbers written on all marked squares.

For example, given the following array:

    A[0] = 1
    A[1] = -2
    A[2] = 0
    A[3] = 9
    A[4] = -1
    A[5] = -2
one possible game could be as follows:

the pebble is on square number 0, which is marked;
we throw 3; the pebble moves from square number 0 to square number 3; we mark square number 3;
we throw 5; the pebble does not move, since there is no square number 8 on the board;
we throw 2; the pebble moves to square number 5; we mark this square and the game ends.
The marked squares are 0, 3 and 5, so the result of the game is 1 + 9 + (−2) = 8. This is the maximal possible result that can be achieved on this board.

Write a function:

def solution(A)

that, given a non-empty array A of N integers, returns the maximal result that can be achieved on the board represented by array A.

For example, given the array

    A[0] = 1
    A[1] = -2
    A[2] = 0
    A[3] = 9
    A[4] = -1
    A[5] = -2
the function should return 8, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [2..100,000];
each element of array A is an integer within the range [−10,000..10,000].
'''

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Implement your solution here
    n = len(A)

    # dp[i] will store the maximal sum that can be achieved when landing on index i.
    # Initialize dp array with negative infinity to correctly handle negative sums
    # and ensure that only reachable states contribute to the maximum.
    dp = [-float('inf')] * n

    # Base case: The game starts at index 0, so the maximal sum when landing on A[0] is A[0] itself.
    dp[0] = A[0]

    # Iterate from the second element up to the last element of the array.
    for i in range(1, n):
        # To reach index 'i', we must have come from a previous index 'j'
        # such that 'i - 6 <= j < i'.
        # We need to find the maximum 'dp[j]' among these possible previous positions.
        
        max_prev_dp = -float('inf') # Initialize to negative infinity for finding maximum

        # Look back up to 6 positions (from i-1 down to i-6, or 0 if i-6 is negative).
        # max(0, i - 6) ensures we don't go out of bounds on the left side.
        for j in range(max(0, i - 6), i):
            max_prev_dp = max(max_prev_dp, dp[j])
        
        # The maximal sum when landing on index 'i' is the value at A[i]
        # plus the maximal sum achieved at the best previous reachable position.
        dp[i] = A[i] + max_prev_dp

    # The final answer is the maximal sum achievable when landing on the last element, A[N-1].
    return dp[n - 1]
