# Prime and Composite Numbers / Count Factors

# Count factors of given number n.

'''
A positive integer D is a factor of a positive integer N if there exists an integer M such that N = D * M.

For example, 6 is a factor of 24, because M = 4 satisfies the above condition (24 = 6 * 4).

Write a function:

def solution(N)

that, given a positive integer N, returns the number of its factors.

For example, given N = 24, the function should return 8, because 24 has 8 factors, namely 1, 2, 3, 4, 6, 8, 12, 24. There are no other factors of 24.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..2,147,483,647].
'''

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    # Implement your solution here
    # Initialize the count of factors.
    count = 0
    
    # Start checking for divisors from 1.
    i = 1

    # We only need to check up to the square root of N.
    # If 'i' is a factor of N, then 'N / i' is also a factor.
    # By checking up to sqrt(N), we find pairs of factors.
    while (i * i <= N):
        if (N % i == 0):
            # If i*i == N, it means i is the square root of N.
            # In this case, i and N/i are the same number, so we count it only once.
            if (i * i == N):
                count += 1
            # If i*i != N, it means i and N/i are two distinct factors.
            # For example, if N=12 and i=2, then 6 (12/2) is also a factor.
            else:
                count += 2
        i += 1 # Move to the next potential divisor

    return count