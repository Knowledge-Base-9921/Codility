# Binary Search Algorithm / Holes in a roof

# O(log(N))

def binary_search(A, x):
    n = len(A)

    _left = 0
    _right = n - 1
    result = -1

    while(_left <= _right):
        _mid = (_left + _right) / 2

        if(A[_mid] <= x):
            _left = _mid + 1
            result = _mid
        else:
            _right = _mid -1

    return result

def boards(A, k):
    return binary_search(A, k)

# Greedy Approach -- O(N)

def boards_greedy(A,k):
    n = len(A)
    boards = 0
    last = -1

    for i in range(n):
        if A[i] == 1 and last < i:
            boards += 1
            last = i + k - 1

    return boards