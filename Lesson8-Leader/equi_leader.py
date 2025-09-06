# Leader / EquiLeader

# Find the index S such that the leaders of the sequences A[0], A[1], ..., A[S] and A[S + 1], A[S + 2], ..., A[N - 1] are the same.

'''
A non-empty array A consisting of N integers is given.

The leader of this array is the value that occurs in more than half of the elements of A.

An equi leader is an index S such that 0 ≤ S < N − 1 and two sequences A[0], A[1], ..., A[S] and A[S + 1], A[S + 2], ..., A[N − 1] have leaders of the same value.

For example, given array A such that:

    A[0] = 4
    A[1] = 3
    A[2] = 4
    A[3] = 4
    A[4] = 4
    A[5] = 2
we can find two equi leaders:

0, because sequences: (4) and (3, 4, 4, 4, 2) have the same leader, whose value is 4.
2, because sequences: (4, 3, 4) and (4, 4, 2) have the same leader, whose value is 4.
The goal is to count the number of equi leaders.

Write a function:

def solution(A)

that, given a non-empty array A consisting of N integers, returns the number of equi leaders.

For example, given:

    A[0] = 4
    A[1] = 3
    A[2] = 4
    A[3] = 4
    A[4] = 4
    A[5] = 2
the function should return 2, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000,000..1,000,000,000].
'''

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Implement your solution here
    n = len(A)

    if n==0:
        return 0

    _candidate = -1
    count = 0

    for i in range(n):
        if count == 0:
            _candidate = A[i]
            count += 1
        elif A[i] == _candidate:
            count += 1
        else:
            count -= 1

    _leader_count = 0
    _leader = -1

    for i in range(n):
        if A[i] == _candidate:
            _leader_count += 1

    if _leader_count > n//2:
        _leader = _candidate
    else:
        return 0

    equi_leader_count = 0
    _leader_count_left = 0

    for i in range(n-1):
        if A[i] == _leader:
            _leader_count_left += 1

        _left_split_count = i + 1
        _right_split_count = n - _left_split_count

        _leader_count_right = _leader_count - _leader_count_left

        is_leader_left = (_leader_count_left * 2 > _left_split_count)
        is_leader_right = (_leader_count_right * 2 > _right_split_count)

        if is_leader_left and is_leader_right:
            equi_leader_count += 1

    return equi_leader_count