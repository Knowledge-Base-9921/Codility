# Greedy Algorithm / Minimum number of double canoes

'''There are n > 0 canoeists weighing respectively 1 <= w0 <= w1 <= . . . <= wn−1 <= 109.
The goal is to seat them in the minimum number of double canoes whose displacement (the
maximum load) equals k. You may assume that wi <= k.
'''

# O(N)

def solution1(W,k):
    canoes = 0
    j = 0

    i = len(W) - 1

    while(i>=j):
        if W[i] + W[j] <= k:
            j += 1
        canoes += 1
        i -= 1

    return canoes

# O(NlogN)

def solution2(W, k):
    """
    Calculates the minimum number of canoes required to transport a group of people.

    Each canoe can carry at most two people, and the total weight in a canoe
    cannot exceed the given limit 'k'.

    Args:
        W: A list of integers representing the weights of people.
           N is the length of W, an integer within the range [1..100,000].
           Each element of W is an integer within the range [1..k].
        k: An integer, the maximum weight capacity of a single canoe.
           k is an integer within the range [1..1,000,000,000].

    Returns:
        The minimum number of canoes needed.
    """
    n = len(W)

    # If there are no people, no canoes are needed.
    if n == 0:
        return 0

    # Step 1: Sort the weights in non-decreasing order.
    # This is crucial for the greedy strategy to work correctly.
    W.sort()

    # Initialize two pointers:
    # 'light_idx' points to the lightest person.
    # 'heavy_idx' points to the heaviest person.
    light_idx = 0
    heavy_idx = n - 1

    # Initialize the count of canoes used.
    canoes_count = 0

    # Step 2: Use a two-pointer approach to greedily pair people.
    # The loop continues as long as the light pointer has not crossed the heavy pointer.
    while light_idx <= heavy_idx:
        # Increment the canoe count for the current trip.
        canoes_count += 1

        # Case 1: Only one person is left.
        # This person must take a canoe alone.
        if light_idx == heavy_idx:
            break

        # Case 2: The lightest person and the heaviest person can share a canoe.
        # If their combined weight is less than or equal to the canoe limit 'k'.
        if W[light_idx] + W[heavy_idx] <= k:
            # Both people go in this canoe. Move the light pointer to the next lightest.
            light_idx += 1
        
        # Case 3: The lightest person and the heaviest person cannot share.
        # This means the heaviest person (W[heavy_idx]) must take a canoe alone,
        # as pairing them with anyone lighter would still exceed the limit (or be less optimal).
        # The heaviest person always needs to be moved out of the way.
        # If they can't pair with the lightest, they can't pair with anyone else either.
        # The light_idx is NOT moved in this case, as the lightest person might still
        # be able to pair with a different (less heavy) person in a future iteration.
        
        # In either Case 2 or Case 3, the heaviest person (W[heavy_idx]) has been assigned a canoe.
        # So, move the heavy pointer to the next heaviest person.
        heavy_idx -= 1

    return canoes_count

