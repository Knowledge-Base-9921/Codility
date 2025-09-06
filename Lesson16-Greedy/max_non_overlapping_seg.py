# Greedy Algorithm / MaxNonoverlappingSegments

# Find a maximal set of non-overlapping segments.

'''
Located on a line are N segments, numbered from 0 to N − 1, whose positions are given in arrays A and B. For each I (0 ≤ I < N) the position of segment I is from A[I] to B[I] (inclusive). The segments are sorted by their ends, which means that B[K] ≤ B[K + 1] for K such that 0 ≤ K < N − 1.

Two segments I and J, such that I ≠ J, are overlapping if they share at least one common point. In other words, A[I] ≤ A[J] ≤ B[I] or A[J] ≤ A[I] ≤ B[J].

We say that the set of segments is non-overlapping if it contains no two overlapping segments. The goal is to find the size of a non-overlapping set containing the maximal number of segments.

For example, consider arrays A, B such that:

    A[0] = 1    B[0] = 5
    A[1] = 3    B[1] = 6
    A[2] = 7    B[2] = 8
    A[3] = 9    B[3] = 9
    A[4] = 9    B[4] = 10
The segments are shown in the figure below.



The size of a non-overlapping set containing a maximal number of segments is 3. For example, possible sets are {0, 2, 3}, {0, 2, 4}, {1, 2, 3} or {1, 2, 4}. There is no non-overlapping set with four segments.

Write a function:

def solution(A, B)

that, given two arrays A and B consisting of N integers, returns the size of a non-overlapping set containing a maximal number of segments.

For example, given arrays A, B shown above, the function should return 3, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..30,000];
each element of arrays A and B is an integer within the range [0..1,000,000,000];
A[I] ≤ B[I], for each I (0 ≤ I < N);
B[K] ≤ B[K + 1], for each K (0 ≤ K < N − 1).
'''

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B):
    # Implement your solution here
    n = len(A)

    # Handle empty input: If there are no segments, 0 non-overlapping segments can be found.
    if n == 0:
        return 0
    
    # Step 1: Combine start and end points into pairs and sort them.
    # Sorting by end points is the key greedy strategy.
    # If segments have the same end point, their order doesn't matter for this problem.
    segments = []
    for i in range(n):
        segments.append((A[i], B[i]))
    
    # Sort the segments primarily by their end points (B[i]).
    # Python's sort is stable, so if end points are equal, original relative order is preserved.
    segments.sort(key=lambda x: x[1])

    # Step 2: Greedily select non-overlapping segments.
    # Initialize the count of selected non-overlapping segments.
    count = 0
    # Initialize 'last_selected_end_point' to a value that ensures the first segment is selected.
    # A very small number (like -1) or the end point of the first segment works.
    # Using the end point of the first segment after incrementing count for it is cleaner.
    
    # Select the first segment (it always contributes to a maximal set because it ends earliest).
    count = 1
    last_selected_end_point = segments[0][1]

    # Iterate through the remaining segments, starting from the second one.
    for i in range(1, n):
        current_segment_start = segments[i][0]
        current_segment_end = segments[i][1]

        # If the current segment's start point is greater than the end point
        # of the last selected segment, it means they do not overlap.
        if current_segment_start > last_selected_end_point:
            # Select this segment.
            count += 1
            # Update the end point of the last selected segment.
            last_selected_end_point = current_segment_end
        # If they overlap (current_segment_start <= last_selected_end_point),
        # we skip the current segment because we've already chosen one that ends earlier.
        # This greedy choice ensures we maximize the remaining space for future segments.

    return count
