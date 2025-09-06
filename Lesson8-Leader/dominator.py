# Leader / Dominator

# Find an index of an array such that its value occurs at more than half of indices in the array.

'''
An array A consisting of N integers is given. The dominator of array A is the value that occurs in more than half of the elements of A.

For example, consider array A such that

 A[0] = 3    A[1] = 4    A[2] =  3
 A[3] = 2    A[4] = 3    A[5] = -1
 A[6] = 3    A[7] = 3
The dominator of A is 3 because it occurs in 5 out of 8 elements of A (namely in those with indices 0, 2, 4, 6 and 7) and 5 is more than a half of 8.

Write a function

def solution(A)

that, given an array A consisting of N integers, returns index of any element of array A in which the dominator of A occurs. The function should return −1 if array A does not have a dominator.

For example, given array A such that

 A[0] = 3    A[1] = 4    A[2] =  3
 A[3] = 2    A[4] = 3    A[5] = -1
 A[6] = 3    A[7] = 3
the function may return 0, 2, 4, 6 or 7, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..100,000];
each element of array A is an integer within the range [−2,147,483,648..2,147,483,647].
'''

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# O(N)

def solution(A):
    # Implement your solution here
    n = len(A)

    _candidate = -1
    _candidate_index = -1
    count = 0

    for i in range(n):
        if count == 0:
            _candidate = A[i]
            _candidate_index = i
            count += 1
        elif A[i] == _candidate:
            count += 1
        else:
            count -= 1

    _leader_count = 0
    _leader_index = -1

    for i in range(n):
        if A[i] == _candidate:
            _leader_count += 1

    if _leader_count > n//2:
        return _candidate_index
    else:
        return -1