# Leader / Golden Algorithm

'''
Let us consider a sequence a0, a1, . . . , an−1. The leader of this sequence is the element whose
value occurs more than n
2 times.
'''

# O(N)

def golden_leader(A):
    n = len(A)

    _candidate = -1
    count = 0

    # Step1: Assume a leader
    for i in range():
        if count == 0:
            _candidate = A[i]
            count = 1
        elif A[i] == _candidate:
            count += 1
        else:
            count -= 1

    # Step2: Verify the leader
    leader_count = 0
    for i in range(n):
        if A[i] == _candidate:
            leader_count+=1

    if leader_count > n//2:
        return _candidate
    else:
        return -1