# Leader / Fast Leader Algorithm

'''
Let us consider a sequence a0, a1, . . . , an−1. The leader of this sequence is the element whose
value occurs more than n
2 times.
'''

# O (Nlog(N))

def fast_leader(A):
    n = len(A)
    _leader = -1

    A.sort()

    _candidate = A[n//2]
    count = 0

    for i in range(n):
        if (A[i] == _candidate):
            count += 1

    if (count > n // 2):
        _leader = _candidate

    return _leader