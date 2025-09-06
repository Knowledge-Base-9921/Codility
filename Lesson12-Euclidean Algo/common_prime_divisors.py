# Euclidean Algorithm / Common Prime Divisors

# Check whether two numbers have the same prime divisors.

'''
A prime is a positive integer X that has exactly two distinct divisors: 1 and X. The first few prime integers are 2, 3, 5, 7, 11 and 13.

A prime D is called a prime divisor of a positive integer P if there exists a positive integer K such that D * K = P. For example, 2 and 5 are prime divisors of 20.

You are given two positive integers N and M. The goal is to check whether the sets of prime divisors of integers N and M are exactly the same.

For example, given:

N = 15 and M = 75, the prime divisors are the same: {3, 5};
N = 10 and M = 30, the prime divisors aren't the same: {2, 5} is not equal to {2, 3, 5};
N = 9 and M = 5, the prime divisors aren't the same: {3} is not equal to {5}.
Write a function:

def solution(A, B)

that, given two non-empty arrays A and B of Z integers, returns the number of positions K for which the prime divisors of A[K] and B[K] are exactly the same.

For example, given:

    A[0] = 15   B[0] = 75
    A[1] = 10   B[1] = 30
    A[2] = 3    B[2] = 5
the function should return 1, because only one pair (15, 75) has the same set of prime divisors.

Write an efficient algorithm for the following assumptions:

Z is an integer within the range [1..100,000];
each element of arrays A and B is an integer within the range [1..2,147,483,647].
'''

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

import math

def solution(A, B):
    # Implement your solution here
    def has_same_prime_divisors(a, b):
        """
        Helper function to check if two integers 'a' and 'b' have the exact
        same set of prime divisors.

        This is achieved by:
        1. Finding the GCD of 'a' and 'b'.
        2. For 'a', repeatedly dividing it by common prime factors it shares with 'b' (via GCD).
           If 'a' reduces to 1, it means all its prime factors were also in 'b'.
        3. Doing the same for 'b'.
        4. If both reduce to 1, they have the same prime divisors.
        """

        # If a and b are equal, they trivially have the same prime divisors.
        if a == b:
            return True
        
        # If one number is 1 and the other is not, they cannot have the same prime divisors
        # (unless both are 1, which is covered by the a == b case).
        if a == 1 or b == 1:
            return False

        # Calculate the Greatest Common Divisor (GCD) of a and b.
        # This GCD contains all common prime factors of a and b.
        g = math.gcd(a, b)

        # Helper to reduce a number by repeatedly dividing by its GCD with a common factor.
        # This effectively removes all prime factors that are common with the 'common_divisor'.
        def reduce_by_common_prime_factors(num, common_divisor):
            while num > 1:
                # Find the GCD of the current 'num' and the 'common_divisor'.
                # This GCD will contain any prime factors that 'num' still shares with 'common_divisor'.
                current_gcd_with_common = math.gcd(num, common_divisor)
                
                # If current_gcd_with_common is 1, it means 'num' no longer shares
                # any prime factors with 'common_divisor'. We can stop.
                if current_gcd_with_common == 1:
                    break
                
                # Divide 'num' by this common factor.
                # This removes one or more prime factors from 'num'.
                num //= current_gcd_with_common
            return num

        # Reduce 'a' by repeatedly dividing by prime factors it shares with 'g'.
        # If 'reduced_a' becomes 1, it means all prime factors of the original 'a'
        # were also prime factors of 'g' (and thus of 'b').
        reduced_a = reduce_by_common_prime_factors(a, g)

        # Reduce 'b' by repeatedly dividing by prime factors it shares with 'g'.
        # If 'reduced_b' becomes 1, it means all prime factors of the original 'b'
        # were also prime factors of 'g' (and thus of 'a').
        reduced_b = reduce_by_common_prime_factors(b, g)

        # If both 'reduced_a' and 'reduced_b' are 1, it means all prime factors
        # of original 'a' were in 'b', and all prime factors of original 'b' were in 'a'.
        # Therefore, they have the exact same set of prime divisors.
        return reduced_a == 1 and reduced_b == 1

    # Main part of the solution function
    count_common_prime_divisors_pairs = 0
    Z = len(A)

    # Iterate through each pair (A[k], B[k])
    for k in range(Z):
        if has_same_prime_divisors(A[k], B[k]):
            count_common_prime_divisors_pairs += 1

    return count_common_prime_divisors_pairs
