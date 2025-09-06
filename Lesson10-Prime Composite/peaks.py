# Prime and Composite Numbers / Peaks

# Divide an array into the maximum number of same-sized blocks, each of which should contain an index P such that A[P - 1] < A[P] > A[P + 1].

'''
A non-empty array A consisting of N integers is given.

A peak is an array element which is larger than its neighbors. More precisely, it is an index P such that 0 < P < N − 1,  A[P − 1] < A[P] and A[P] > A[P + 1].

For example, the following array A:

    A[0] = 1
    A[1] = 2
    A[2] = 3
    A[3] = 4
    A[4] = 3
    A[5] = 4
    A[6] = 1
    A[7] = 2
    A[8] = 3
    A[9] = 4
    A[10] = 6
    A[11] = 2
has exactly three peaks: 3, 5, 10.

We want to divide this array into blocks containing the same number of elements. More precisely, we want to choose a number K that will yield the following blocks:

A[0], A[1], ..., A[K − 1],
A[K], A[K + 1], ..., A[2K − 1],
...
A[N − K], A[N − K + 1], ..., A[N − 1].
What's more, every block should contain at least one peak. Notice that extreme elements of the blocks (for example A[K − 1] or A[K]) can also be peaks, but only if they have both neighbors (including one in an adjacent blocks).

The goal is to find the maximum number of blocks into which the array A can be divided.

Array A can be divided into blocks as follows:

one block (1, 2, 3, 4, 3, 4, 1, 2, 3, 4, 6, 2). This block contains three peaks.
two blocks (1, 2, 3, 4, 3, 4) and (1, 2, 3, 4, 6, 2). Every block has a peak.
three blocks (1, 2, 3, 4), (3, 4, 1, 2), (3, 4, 6, 2). Every block has a peak. Notice in particular that the first block (1, 2, 3, 4) has a peak at A[3], because A[2] < A[3] > A[4], even though A[4] is in the adjacent block.
However, array A cannot be divided into four blocks, (1, 2, 3), (4, 3, 4), (1, 2, 3) and (4, 6, 2), because the (1, 2, 3) blocks do not contain a peak. Notice in particular that the (4, 3, 4) block contains two peaks: A[3] and A[5].

The maximum number of blocks that array A can be divided into is three.

Write a function:

def solution(A)

that, given a non-empty array A consisting of N integers, returns the maximum number of blocks into which A can be divided.

If A cannot be divided into some number of blocks, the function should return 0.

For example, given:

    A[0] = 1
    A[1] = 2
    A[2] = 3
    A[3] = 4
    A[4] = 3
    A[5] = 4
    A[6] = 1
    A[7] = 2
    A[8] = 3
    A[9] = 4
    A[10] = 6
    A[11] = 2
the function should return 3, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [0..1,000,000,000].
'''

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

import math

def solution(A):
    # Implement your solution here
    n = len(A)

    # If the array has less than 3 elements, no peaks can exist.
    # Therefore, no blocks can be formed to satisfy the condition.
    if n < 3:
        return 0

    # Step 1: Identify all peaks in the array.
    # A peak A[i] is defined as A[i-1] < A[i] > A[i+1].
    # Peaks cannot be at the first (index 0) or last (index n-1) elements.
    peaks_bool = [False] * n  # Boolean array to mark peak positions
    num_actual_peaks = 0      # Counter for the total number of peaks found

    for i in range(1, n - 1):
        if A[i] > A[i-1] and A[i] > A[i+1]:
            peaks_bool[i] = True
            num_actual_peaks += 1

    # If no peaks are found in the entire array, no blocks can contain a peak.
    if num_actual_peaks == 0:
        return 0

    # Step 2: Precompute a prefix sum array for peaks.
    # prefix_peaks_count[i] will store the number of peaks in A[0...i-1].
    # This allows for O(1) checking if a range contains a peak.
    prefix_peaks_count = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix_peaks_count[i] = prefix_peaks_count[i-1] + (1 if peaks_bool[i-1] else 0)

    # Helper function to check if a given number of blocks (K) is possible.
    # It verifies if N is divisible by K and if each of the K blocks contains at least one peak.
    def check_k_blocks(K):
        # If N is not divisible by K, we cannot form K same-sized blocks.
        if n % K != 0:
            return False
        
        block_size = n // K
        
        # Iterate through each of the K blocks.
        for block_idx in range(K):
            # Calculate the start and end indices of the current block.
            block_start = block_idx * block_size
            block_end = (block_idx + 1) * block_size - 1
            
            # Check if there is at least one peak in the current block
            # using the precomputed prefix_peaks_count array.
            # If prefix_peaks_count[block_end + 1] - prefix_peaks_count[block_start] is 0,
            # it means no peaks are present in this block.
            if prefix_peaks_count[block_end + 1] - prefix_peaks_count[block_start] == 0:
                return False # This K is not possible because a block lacks a peak.
        
        return True # All K blocks contain at least one peak.

    # Step 3: Find the maximum K (number of blocks) that satisfies the conditions.
    # We iterate through possible values of K.
    # K must be a divisor of N, and K must be less than or equal to the total number of peaks.
    # We iterate up to sqrt(N) to find divisors efficiently.
    max_possible_blocks = 0
    
    i = 1
    while i * i <= n:
        if n % i == 0:
            # Case 1: K = i (current divisor)
            k1 = i
            # Check if this K is a valid number of blocks (K <= total peaks)
            if k1 <= num_actual_peaks:
                if check_k_blocks(k1):
                    max_possible_blocks = max(max_possible_blocks, k1)

            # Case 2: K = N // i (the corresponding pair divisor)
            k2 = n // i
            # Avoid double-checking if i*i == n (i.e., k1 == k2)
            # Also check if this K is a valid number of blocks (K <= total peaks)
            if k2 != k1 and k2 <= num_actual_peaks:
                if check_k_blocks(k2):
                    max_possible_blocks = max(max_possible_blocks, k2)
        i += 1
        
    return max_possible_blocks