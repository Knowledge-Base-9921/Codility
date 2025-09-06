# Fibonacci Numbers / Ladder

# Count the number of different ways of climbing to the top of a ladder.

'''
You have to climb up a ladder. The ladder has exactly N rungs, numbered from 1 to N. With each step, you can ascend by one or two rungs. More precisely:

with your first step you can stand on rung 1 or 2,
if you are on rung K, you can move to rungs K + 1 or K + 2,
finally you have to stand on rung N.
Your task is to count the number of different ways of climbing to the top of the ladder.

For example, given N = 4, you have five different ways of climbing, ascending by:

1, 1, 1 and 1 rung,
1, 1 and 2 rungs,
1, 2 and 1 rung,
2, 1 and 1 rungs, and
2 and 2 rungs.
Given N = 5, you have eight different ways of climbing, ascending by:

1, 1, 1, 1 and 1 rung,
1, 1, 1 and 2 rungs,
1, 1, 2 and 1 rung,
1, 2, 1 and 1 rung,
1, 2 and 2 rungs,
2, 1, 1 and 1 rungs,
2, 1 and 2 rungs, and
2, 2 and 1 rung.
The number of different ways can be very large, so it is sufficient to return the result modulo 2P, for a given integer P.

Write a function:

def solution(A, B)

that, given two non-empty arrays A and B of L integers, returns an array consisting of L integers specifying the consecutive answers; position I should contain the number of different ways of climbing the ladder with A[I] rungs modulo 2B[I].

For example, given L = 5 and:

    A[0] = 4   B[0] = 3
    A[1] = 4   B[1] = 2
    A[2] = 5   B[2] = 4
    A[3] = 5   B[3] = 3
    A[4] = 1   B[4] = 1
the function should return the sequence [5, 1, 8, 0, 1], as explained above.

Write an efficient algorithm for the following assumptions:

L is an integer within the range [1..50,000];
each element of array A is an integer within the range [1..L];
each element of array B is an integer within the range [1..30].
'''

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B):
    # Implement your solution here
    M = len(A)
    max_ladder_length = 0
    if M > 0:
        # Find the maximum ladder length to determine the size for precomputation.
        max_ladder_length = max(A)

    # Step 1: Precompute Fibonacci numbers up to (max_ladder_length + 1)
    # The number of ways to climb L rungs is F(L+1).
    # We need F(i) where i goes up to max_ladder_length + 1.
    # The largest possible modulo is 2**30.
    # If we compute Fibonacci numbers modulo 2**30, we can then easily get
    # the result modulo any 2**B[k] where B[k] <= 30.
    
    # fib_mod_max_power[i] will store F(i) % (2**30).
    # Array size is max_ladder_length + 2 to accommodate F(0) up to F(max_ladder_length + 1).
    fib_mod_max_power = [0] * (max_ladder_length + 2)
    
    # Base cases for Fibonacci sequence: F(0) = 0, F(1) = 1
    fib_mod_max_power[0] = 0
    fib_mod_max_power[1] = 1

    # The maximum modulo for precomputation is 2**30.
    # This is because B[k] is at most 30.
    MOD_PRECOMPUTE = 1 << 30 # Equivalent to 2**30

    # Generate Fibonacci numbers modulo MOD_PRECOMPUTE
    for i in range(2, max_ladder_length + 2):
        fib_mod_max_power[i] = (fib_mod_max_power[i-1] + fib_mod_max_power[i-2]) % MOD_PRECOMPUTE

    # Step 2: Answer each query using the precomputed Fibonacci numbers.
    results = []
    for k in range(M):
        ladder_length = A[k]
        mod_power = B[k]
        
        # The number of ways to climb 'ladder_length' rungs is F(ladder_length + 1).
        # We need this value modulo 2**mod_power.
        
        # The value fib_mod_max_power[ladder_length + 1] already contains
        # F(ladder_length + 1) % (2**30).
        # To get the result modulo 2**mod_power, we simply apply the modulo again.
        # (X % (2**Y)) is equivalent to (X & ((1 << Y) - 1)) for powers of 2.
        
        # Calculate the specific modulo for the current query
        current_modulo = 1 << mod_power # This is 2**mod_power
        
        # Get the precomputed Fibonacci number and apply the specific modulo
        ways = fib_mod_max_power[ladder_length + 1] % current_modulo
        
        results.append(ways)

    return results