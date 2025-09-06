# Bitwise Ops / CountConformingBitmasks

# Count 30-bit bitmasks conforming to at least one of three given 30-bit bitmasks.

'''
In this problem we consider unsigned 30-bit integers, i.e. all integers B such that 0 ≤ B < 230.

We say that integer A conforms to integer B if, in all positions where B has bits set to 1, A has corresponding bits set to 1.

For example:

00 0000 1111 0111 1101 1110 0000 1111(BIN) = 16,244,239 conforms to
00 0000 1100 0110 1101 1110 0000 0001(BIN) = 13,032,961, but
11 0000 1101 0111 0000 1010 0000 0101(BIN) = 819,399,173 does not conform to
00 0000 1001 0110 0011 0011 0000 1111(BIN) = 9,843,471.
Write a function:

def solution(A, B, C)

that, given three unsigned 30-bit integers A, B and C, returns the number of unsigned 30-bit integers conforming to at least one of the given integers.

For example, for integers:

A = 11 1111 1111 1111 1111 1111 1001 1111(BIN) = 1,073,741,727,
B = 11 1111 1111 1111 1111 1111 0011 1111(BIN) = 1,073,741,631, and
C = 11 1111 1111 1111 1111 1111 0110 1111(BIN) = 1,073,741,679,
the function should return 8, since there are 8 unsigned 30-bit integers conforming to A, B or C, namely:

11 1111 1111 1111 1111 1111 0011 1111(BIN) = 1,073,741,631,
11 1111 1111 1111 1111 1111 0110 1111(BIN) = 1,073,741,679,
11 1111 1111 1111 1111 1111 0111 1111(BIN) = 1,073,741,695,
11 1111 1111 1111 1111 1111 1001 1111(BIN) = 1,073,741,727,
11 1111 1111 1111 1111 1111 1011 1111(BIN) = 1,073,741,759,
11 1111 1111 1111 1111 1111 1101 1111(BIN) = 1,073,741,791,
11 1111 1111 1111 1111 1111 1110 1111(BIN) = 1,073,741,807,
11 1111 1111 1111 1111 1111 1111 1111(BIN) = 1,073,741,823.
Write an efficient algorithm for the following assumptions:

A, B and C are integers within the range [0..1,073,741,823].
'''

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def popcount(n):
    """
    Counts the number of set bits (1s) in an integer using Brian Kernighan's algorithm.
    This algorithm iteratively clears the least significant set bit until the number becomes 0.
    The number of iterations is equal to the number of set bits.

    Args:
        n: An integer.

    Returns:
        The number of set bits in n.
    """
    count = 0
    while n > 0:
        # n & (n - 1) clears the least significant set bit.
        # Example: n = 0b10100 (20)
        # n - 1 = 0b10011 (19)
        # n & (n - 1) = 0b10100 & 0b10011 = 0b10000 (16)
        n &= (n - 1)
        count += 1
    return count

def solution(A, B, C):
    """
    Counts the number of unsigned 30-bit integers X that conform to at least
    one of the given integers A, B, or C.

    An integer X conforms to an integer M if (X & M) == M.
    The total number of such integers X (from 0 to 2^30 - 1) is 2^(30 - popcount(M)).

    This function uses the Principle of Inclusion-Exclusion:
    |S_A U S_B U S_C| = |S_A| + |S_B| + |S_C|
                       - (|S_A intersect S_B| + |S_A intersect S_C| + |S_B intersect S_C|)
                       + |S_A intersect S_B intersect S_C|

    Where:
    - |S_M| = 2^(30 - popcount(M))
    - |S_M1 intersect S_M2| = 2^(30 - popcount(M1 | M2))
    - |S_M1 intersect S_M2 intersect S_M3| = 2^(30 - popcount(M1 | M2 | M3))

    Args:
        A, B, C: Three unsigned 30-bit integers (0 <= value < 2^30).

    Returns:
        The total count of conforming bitmasks.
    """
    # Calculate population counts for individual masks
    pc_A = popcount(A)
    pc_B = popcount(B)
    pc_C = popcount(C)

    # Calculate population counts for pairwise bitwise OR operations
    # An integer X conforms to both M1 and M2 if it conforms to (M1 | M2).
    pc_A_or_B = popcount(A | B)
    pc_A_or_C = popcount(A | C)
    pc_B_or_C = popcount(B | C)

    # Calculate population count for the triple bitwise OR operation
    # An integer X conforms to M1, M2, and M3 if it conforms to (M1 | M2 | M3).
    pc_A_or_B_or_C = popcount(A | B | C)

    # Apply the Principle of Inclusion-Exclusion
    # Sum of individual set sizes
    sum_singles = (2**(30 - pc_A) + 2**(30 - pc_B) + 2**(30 - pc_C))

    # Sum of pairwise intersection sizes (subtracted)
    sum_pairs = (2**(30 - pc_A_or_B) + 2**(30 - pc_A_or_C) + 2**(30 - pc_B_or_C))

    # Size of the triple intersection (added back)
    sum_triples = 2**(30 - pc_A_or_B_or_C)

    # Final count
    count = sum_singles - sum_pairs + sum_triples

    return count