# Binary Search Algorithm / Min Max Division

# Divide array A into K blocks and minimize the largest sum of any block.

'''
You are given integers K, M and a non-empty array A consisting of N integers. Every element of the array is not greater than M.

You should divide this array into K blocks of consecutive elements. The size of the block is any integer between 0 and N. Every element of the array should belong to some block.

The sum of the block from X to Y equals A[X] + A[X + 1] + ... + A[Y]. The sum of empty block equals 0.

The large sum is the maximal sum of any block.

For example, you are given integers K = 3, M = 5 and array A such that:

  A[0] = 2
  A[1] = 1
  A[2] = 5
  A[3] = 1
  A[4] = 2
  A[5] = 2
  A[6] = 2
The array can be divided, for example, into the following blocks:

[2, 1, 5, 1, 2, 2, 2], [], [] with a large sum of 15;
[2], [1, 5, 1, 2], [2, 2] with a large sum of 9;
[2, 1, 5], [], [1, 2, 2, 2] with a large sum of 8;
[2, 1], [5, 1], [2, 2, 2] with a large sum of 6.
The goal is to minimize the large sum. In the above example, 6 is the minimal large sum.

Write a function:

def solution(K, M, A)

that, given integers K, M and a non-empty array A consisting of N integers, returns the minimal large sum.

For example, given K = 3, M = 5 and array A such that:

  A[0] = 2
  A[1] = 1
  A[2] = 5
  A[3] = 1
  A[4] = 2
  A[5] = 2
  A[6] = 2
the function should return 6, as explained above.

Write an efficient algorithm for the following assumptions:

N and K are integers within the range [1..100,000];
M is an integer within the range [0..10,000];
each element of array A is an integer within the range [0..M].
'''

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(K, M, A):
    # Implement your solution here
    n = len(A)

    # Helper function to check if it's possible to divide the array into K blocks
    # such that no block sum exceeds 'max_block_sum'.
    def check(max_block_sum):
        blocks_needed = 1  # Start with the first block
        current_block_sum = 0

        for x in A:
            # If an individual element is greater than max_block_sum,
            # it's impossible to satisfy the condition with this max_block_sum.
            # This check is technically redundant if low is initialized correctly (max(A)),
            # but it adds robustness.
            if x > max_block_sum:
                return False

            if current_block_sum + x <= max_block_sum:
                # Add the current element to the current block
                current_block_sum += x
            else:
                # If adding the current element exceeds max_block_sum,
                # start a new block.
                blocks_needed += 1
                current_block_sum = x # The current element becomes the start of the new block
        
        # Return True if the number of blocks needed is less than or equal to K.
        return blocks_needed <= K

    # Define the range for binary search on the result (the minimal largest sum).
    # 'low' is the minimum possible largest sum: the maximum single element in A.
    # If A is empty, low can be 0.
    low = 0
    if n > 0:
        low = max(A)
    
    # 'high' is the maximum possible largest sum: the sum of all elements in A.
    # This occurs if K=1 (all elements in one block).
    high = sum(A)

    # 'min_max_sum' will store the best (minimal) largest sum found so far.
    # Initialize it to high, as it's a valid (though not necessarily optimal) upper bound.
    min_max_sum = high

    # Perform binary search.
    while low <= high:
        mid = (low + high) // 2
        
        # Check if it's possible to divide A into K blocks with 'mid' as the max sum.
        if check(mid):
            # If it's possible, 'mid' is a potential answer.
            # We try to find an even smaller max sum, so we store 'mid'
            # and search in the lower half.
            min_max_sum = mid
            high = mid - 1
        else:
            # If it's not possible, 'mid' is too small.
            # We need a larger max sum, so search in the upper half.
            low = mid + 1

    return min_max_sum
