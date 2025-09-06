# Binary Search Algorithm / Binary Search

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