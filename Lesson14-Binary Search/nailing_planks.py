# Binary Search Algorithm / NailingPlanks

# Count the minimum number of nails that allow a series of planks to be nailed.

'''
You are given two non-empty arrays A and B consisting of N integers. These arrays represent N planks. More precisely, A[K] is the start and B[K] the end of the K−th plank.

Next, you are given a non-empty array C consisting of M integers. This array represents M nails. More precisely, C[I] is the position where you can hammer in the I−th nail.

We say that a plank (A[K], B[K]) is nailed if there exists a nail C[I] such that A[K] ≤ C[I] ≤ B[K].

The goal is to find the minimum number of nails that must be used until all the planks are nailed. In other words, you should find a value J such that all planks will be nailed after using only the first J nails. More precisely, for every plank (A[K], B[K]) such that 0 ≤ K < N, there should exist a nail C[I] such that I < J and A[K] ≤ C[I] ≤ B[K].

For example, given arrays A, B such that:

    A[0] = 1    B[0] = 4
    A[1] = 4    B[1] = 5
    A[2] = 5    B[2] = 9
    A[3] = 8    B[3] = 10
four planks are represented: [1, 4], [4, 5], [5, 9] and [8, 10].

Given array C such that:

    C[0] = 4
    C[1] = 6
    C[2] = 7
    C[3] = 10
    C[4] = 2
if we use the following nails:

0, then planks [1, 4] and [4, 5] will both be nailed.
0, 1, then planks [1, 4], [4, 5] and [5, 9] will be nailed.
0, 1, 2, then planks [1, 4], [4, 5] and [5, 9] will be nailed.
0, 1, 2, 3, then all the planks will be nailed.
Thus, four is the minimum number of nails that, used sequentially, allow all the planks to be nailed.

Write a function:

def solution(A, B, C)

that, given two non-empty arrays A and B consisting of N integers and a non-empty array C consisting of M integers, returns the minimum number of nails that, used sequentially, allow all the planks to be nailed.

If it is not possible to nail all the planks, the function should return −1.

For example, given arrays A, B, C such that:

    A[0] = 1    B[0] = 4
    A[1] = 4    B[1] = 5
    A[2] = 5    B[2] = 9
    A[3] = 8    B[3] = 10

    C[0] = 4
    C[1] = 6
    C[2] = 7
    C[3] = 10
    C[4] = 2
the function should return 4, as explained above.

Write an efficient algorithm for the following assumptions:

N and M are integers within the range [1..30,000];
each element of arrays A, B and C is an integer within the range [1..2*M];
A[K] ≤ B[K].
'''

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B, C):
    # Implement your solution here
    n = len(A) # Number of planks
    m = len(C) # Number of nails

    # The maximum possible coordinate value for positions in A, B, C.
    # Problem constraints state elements are within [1..2 * N].
    # So, the maximum coordinate value is 2 * n.
    max_coord_val = max(max(B), max(C))

    # Helper function to check if it's possible to nail all planks
    # using only the first `num_nails_limit` nails from array C.
    def check(num_nails_limit):
        # `nail_count_at_pos[p]` will store 1 if there's at least one nail
        # at position `p` among the first `num_nails_limit` nails, 0 otherwise.
        # We initialize with zeros.
        # Array size is max_coord_val + 1 to cover indices from 0 to max_coord_val.
        nail_count_at_pos = [0] * (max_coord_val + 1) 
        
        # Mark the positions of the first `num_nails_limit` nails.
        # Note: If multiple nails are at the same position, we just need to mark it once.
        for k in range(num_nails_limit):
            # C[k] can be up to max_coord_val (2*n)
            nail_count_at_pos[C[k]] = 1

        # Build a prefix sum array for nail presence.
        # `prefix_nail_presence_sum[p]` stores the total count of distinct nail positions
        # from position 0 up to position `p` (considering only the first `num_nails_limit` nails).
        # prefix_nail_presence_sum[0] is 0, representing no nails before position 1.
        prefix_nail_presence_sum = [0] * (max_coord_val + 1)
        for p in range(1, max_coord_val + 1): # Iterate from 1 to max_coord_val
            prefix_nail_presence_sum[p] = prefix_nail_presence_sum[p-1] + nail_count_at_pos[p]

        # Now, check if each plank is nailed.
        for i in range(n):
            plank_start = A[i]
            plank_end = B[i]
            
            # A plank is nailed if there is at least one nail in its range [plank_start, plank_end].
            # We can check this efficiently using the prefix sum array:
            # The number of nails in the range [plank_start, plank_end] is
            # prefix_nail_presence_sum[plank_end] - prefix_nail_presence_sum[plank_start - 1].
            # If this difference is greater than 0, the plank is nailed.
            # plank_start can be 1, so plank_start - 1 can be 0.
            # prefix_nail_presence_sum[0] is correctly initialized to 0.
            if prefix_nail_presence_sum[plank_end] - prefix_nail_presence_sum[plank_start - 1] == 0:
                return False # This plank is not nailed, so `num_nails_limit` is not enough.
        
        return True # All planks are nailed with `num_nails_limit` nails.

    # Binary search for the minimum number of nails.
    # The problem has a monotonic property: if `X` nails are sufficient, then `X+1` nails are also sufficient.
    # This allows us to binary search on the number of nails.
    
    low = 1 # Minimum possible number of nails (at least one is needed if N > 0)
    high = m # Maximum possible number of nails (all available nails)
    result_min_nails = -1 # Initialize to -1, indicating no solution found yet

    # Handle the case of an empty array A (no planks).
    # Although constraints say N is [1..100,000], it's good practice.
    if n == 0:
        return 0 # No planks, 0 nails needed.

    while low <= high:
        mid = (low + high) // 2 # The number of nails we are currently testing
        
        if check(mid):
            # If `mid` nails are sufficient, then `mid` is a possible answer.
            # We store this as a potential result and try to find an even smaller number of nails
            # by searching in the lower half of the range.
            result_min_nails = mid
            high = mid - 1
        else:
            # If `mid` nails are not sufficient, it means we need more nails.
            # We search in the upper half of the range.
            low = mid + 1

    return result_min_nails