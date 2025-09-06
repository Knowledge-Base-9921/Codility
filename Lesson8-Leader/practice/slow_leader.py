# Leader / Slow Leader Algorithm

'''
Let us consider a sequence a0, a1, . . . , an−1. The leader of this sequence is the element whose
value occurs more than n
2 times.
'''

# O(n^2)

def slow_leader(A):
    n = len(A)
    _leader = -1

    for i in range(n):
        _candidate = A[i]
        count = 0

        for j in range(n):
            if A[j] == _candidate:
                count += 1
        
        if (count > n // 2):
            _leader = _candidate

    return _leader