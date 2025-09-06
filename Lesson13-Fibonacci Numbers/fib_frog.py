# Fibonacci Numbers / FibFrog

# Count the minimum number of jumps required for a frog to get to the other side of a river.

'''
The Fibonacci sequence is defined using the following recursive formula:

    F(0) = 0
    F(1) = 1
    F(M) = F(M - 1) + F(M - 2) if M >= 2
A small frog wants to get to the other side of a river. The frog is initially located at one bank of the river (position −1) and wants to get to the other bank (position N). The frog can jump over any distance F(K), where F(K) is the K-th Fibonacci number. Luckily, there are many leaves on the river, and the frog can jump between the leaves, but only in the direction of the bank at position N.

The leaves on the river are represented in an array A consisting of N integers. Consecutive elements of array A represent consecutive positions from 0 to N − 1 on the river. Array A contains only 0s and/or 1s:

0 represents a position without a leaf;
1 represents a position containing a leaf.
The goal is to count the minimum number of jumps in which the frog can get to the other side of the river (from position −1 to position N). The frog can jump between positions −1 and N (the banks of the river) and every position containing a leaf.

For example, consider array A such that:

    A[0] = 0
    A[1] = 0
    A[2] = 0
    A[3] = 1
    A[4] = 1
    A[5] = 0
    A[6] = 1
    A[7] = 0
    A[8] = 0
    A[9] = 0
    A[10] = 0
The frog can make three jumps of length F(5) = 5, F(3) = 2 and F(5) = 5.

Write a function:

def solution(A)

that, given an array A consisting of N integers, returns the minimum number of jumps by which the frog can get to the other side of the river. If the frog cannot reach the other side of the river, the function should return −1.

For example, given:

    A[0] = 0
    A[1] = 0
    A[2] = 0
    A[3] = 1
    A[4] = 1
    A[5] = 0
    A[6] = 1
    A[7] = 0
    A[8] = 0
    A[9] = 0
    A[10] = 0
the function should return 3, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..100,000];
each element of array A is an integer that can have one of the following values: 0, 1.
'''

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import collections

def solution(A):
    # Implement your solution here
    n = len(A)

    # Step 1: Generate Fibonacci numbers.
    # We need Fibonacci numbers up to N + 1 (since the frog can jump from 0 to N-1,
    # and the target is N, the largest jump needed could be N itself from position 0).
    fib_set = set() # Use a set for O(1) average-case lookup
    fib_list = []   # Use a list to iterate in increasing order

    a, b = 0, 1
    fib_list.append(a) # F(0) = 0 (though not useful for jumps, good for completeness)
    fib_set.add(a)

    fib_list.append(b) # F(1) = 1
    fib_set.add(b)

    while b <= n + 1: # Generate Fibonacci numbers up to N+1
        next_fib = a + b
        if next_fib > n + 1: # Optimization: stop if the next Fibonacci number exceeds max jump distance
            break
        fib_list.append(next_fib)
        fib_set.add(next_fib)
        a = b
        b = next_fib
    
    # Remove F(0) if it was added, as a jump of 0 is not allowed.
    if 0 in fib_list:
        fib_list.remove(0)
    
    # Sort fib_list in descending order for BFS to potentially find longer jumps first,
    # though ascending order also works and is more common for BFS.
    # For this problem, the order doesn't strictly matter for correctness,
    # but it can sometimes slightly optimize which path is explored first.
    # Let's keep it sorted for clarity.
    fib_list.sort()


    # Step 2: Use Breadth-First Search (BFS) to find the minimum number of jumps.
    # The state in the BFS queue will be (current_position, jumps_count).
    # The frog starts at position -1 (before the river).
    
    # Queue for BFS: stores (current_position, jumps_made)
    queue = collections.deque([(-1, 0)])
    
    # Visited array to avoid cycles and redundant computations.
    # visited[i] will be True if position 'i' has been visited.
    # Size N+1 for positions 0 to N-1, plus an extra for the "start" position -1.
    # We can map -1 to N for visited array or handle it separately.
    # A more straightforward way is to use a set for visited positions.
    visited_positions = set()
    visited_positions.add(-1) # Mark the starting position as visited

    while queue:
        current_pos, jumps_made = queue.popleft()

        # Try all possible Fibonacci jumps
        for jump_len in fib_list:
            next_pos = current_pos + jump_len

            # Case 1: Reached the other side (position N)
            if next_pos == n:
                return jumps_made + 1 # Found the target, return jumps + 1 (for the final jump)

            # Case 2: Landed on a leaf within the river
            # Check if next_pos is within bounds [0, N-1]
            # Check if there's a leaf at next_pos (A[next_pos] == 1)
            # Check if this position has not been visited yet to avoid cycles and re-exploring longer paths
            if 0 <= next_pos < n and A[next_pos] == 1 and next_pos not in visited_positions:
                visited_positions.add(next_pos) # Mark as visited
                queue.append((next_pos, jumps_made + 1)) # Add to queue for further exploration

    # If the queue becomes empty and the target (position N) was not reached,
    # it means the frog cannot get to the other side.
    return -1