# Arrays / Reversing an Array

'''
: Given array A consisting of N integers, return the reversed array.
'''

A = [1,6,3,5,8,2,9,0,4,7]
n = len(A)

for _left in range(n//2):
    _right = n-_left-1
    A[_left], A[_right] = A[_right], A[_left]

print(A) 