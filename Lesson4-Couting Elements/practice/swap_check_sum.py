# Counting Elements / Swap the elements and check if sums match

'''
You are given an integer m (1 <= m <= 1 000 000) and two non-empty, zero-indexed
arrays A and B of n integers, a0, a1, . . . , an-1 and b0, b1, . . . , bn-1 respectively (0 <= ai, bi <= m).
The goal is to check whether there is a swap operation which can be performed on these
arrays in such a way that the sum of elements in array A equals the sum of elements in
array B after the swap. By swap operation we mean picking one element from array A and
one element from array B and exchanging them.
'''

## slow solution: O(n^2)

def slow_solution(A, B, m):
    n = len(A) # same as len(B)

    sum_A = sum(A)
    sum_B = sum(B)

    for i in range(n):
        for j in range(n):
            _delta = B[j] - A[i]

            sum_A += _delta # _delta has negative A[i]
            sum_B -= _delta # _delta has positive B[j]

            if sum_A == sum_B:
                return True

            # Reset
            sum_A -= _delta
            sum_B += _delta
    
    return False

# Fast Solution: O(m + n)

def counting(A,m):
    n = len(A) # O(1)
    A_count = [0] * (m+1) # O(m)

    for i in range(n): # O(n)
        A_count[A[i]]+=1 # O(1)

    return A_count

def fast_solution(A, B, m):
    n = len(A)

    sum_A = sum(A)
    sum_B = sum(B)

    # Logic

    '''
    if we swap an element 'x' from A with element 'y' from B
    for the sums to be equal after the swap
        sum_A_new = sum_A - x + y
        sum_B_new = sum_B - y + x

    Condition: sum_A_new = sum_B_new -> sum_A - x + y = sum_B - y + x -> 2y - 2x = sum_B - sum_A
        2(y-x) = sum_B - sum_A
        
        If y-x is _delta
        2*_delta = sum_B - sum_A -> _delta = (sum_B - sum_A) / 2

    If sum_B - sum_A is odd, _delta won't be an integer but a floating point as the division is by 2 -> impossible to get equal sums
    If sum_B - sum_A is even, _delta will be an integer, so there is a chance to get equal sums

    '''
     
    _delta = sum_B - sum_A
    
    if _delta % 2 == 1:
        return False
    
    _delta //= 2

    A_count = counting(A,m)

    for i in range(n):
        _B_delta = B[i] - _delta # y - (y-x) -> x -> _B_Delta is x now
        if 0<=_B_delta and _B_delta<=m and A_count[_B_delta] > 0: # checks if A_count[x] exists, where x is the element from A itself
            return True
        
    return False