# Prime and Composite Numbers / Flags

# Find the maximum number of flags that can be set on mountain peaks.

'''
A non-empty array A consisting of N integers is given.

A peak is an array element which is larger than its neighbours. More precisely, it is an index P such that 0 < P < N − 1 and A[P − 1] < A[P] > A[P + 1].

For example, the following array A:

    A[0] = 1
    A[1] = 5
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
has exactly four peaks: elements 1, 3, 5 and 10.

You are going on a trip to a range of mountains whose relative heights are represented by array A, as shown in a figure below. You have to choose how many flags you should take with you. The goal is to set the maximum number of flags on the peaks, according to certain rules.

Flags can only be set on peaks. What's more, if you take K flags, then the distance between any two flags should be greater than or equal to K. The distance between indices P and Q is the absolute value |P − Q|.

For example, given the mountain range represented by array A, above, with N = 12, if you take:

two flags, you can set them on peaks 1 and 5;
three flags, you can set them on peaks 1, 5 and 10;
four flags, you can set only three flags, on peaks 1, 5 and 10.
You can therefore set a maximum of three flags in this case.

Write a function:

def solution(A)

that, given a non-empty array A of N integers, returns the maximum number of flags that can be set on the peaks of the array.

For example, the following array A:

    A[0] = 1
    A[1] = 5
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

N is an integer within the range [1..400,000];
each element of array A is an integer within the range [0..1,000,000,000].
'''

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Implement your solution here
    n = len(A)

    # Step 1: Find all peaks in the array.
    # A peak A[i] must satisfy A[i-1] < A[i] > A[i+1].
    # Peaks cannot be at the first or last index.
    peaks = []
    for i in range(1, n - 1):
        if A[i] > A[i-1] and A[i] > A[i+1]:
            peaks.append(i)

    # If there are no peaks, or too few peaks to place any flags (less than 2),
    # then 0 flags can be set.
    if len(peaks) < 2:
        return len(peaks) # If 0 or 1 peak, max flags is just that number of peaks

    # Step 2: Use binary search to find the maximum number of flags (K) that can be set.
    # The possible number of flags K ranges from 1 up to the total number of peaks.
    # If we can place K flags, we can also place K-1 flags. This monotonicity allows binary search.
    
    # 'low' is the minimum possible number of flags (1).
    # 'high' is the maximum possible number of flags (which is the total number of peaks).
    low = 1
    high = len(peaks)
    max_flags = 0 # Stores the maximum number of flags found so far

    while low <= high:
        # 'mid' is the number of flags we are currently trying to place.
        mid = (low + high) // 2
        
        # If mid is 0, it doesn't make sense to try to place 0 flags,
        # or it implies we should try a larger number if possible.
        if mid == 0: 
            low = mid + 1
            continue

        # Try to place 'mid' flags.
        # 'flags_placed_count' tracks how many flags we successfully place for current 'mid'.
        flags_placed_count = 0
        # 'last_flag_index' stores the index of the last peak where a flag was placed.
        # Initialize it to a value that allows the first peak to be chosen.
        # A value like -mid ensures the first peak is at least 'mid' distance away from a non-existent flag.
        last_flag_index = -mid 

        # Iterate through the identified peaks.
        for peak_index in peaks:
            # Check if the current peak is far enough from the last placed flag.
            # The distance must be at least 'mid' (the number of flags we are trying to place).
            if peak_index - last_flag_index >= mid:
                flags_placed_count += 1
                last_flag_index = peak_index
            
            # If we have successfully placed 'mid' flags, we can stop checking for this 'mid'.
            if flags_placed_count == mid:
                break
        
        # After trying to place 'mid' flags:
        if flags_placed_count == mid:
            # If we successfully placed 'mid' flags, it means it's possible.
            # We store this as a potential answer and try to place more flags.
            max_flags = mid
            low = mid + 1
        else:
            # If we could not place 'mid' flags, it means 'mid' is too high.
            # We need to try placing fewer flags.
            high = mid - 1

    return max_flags