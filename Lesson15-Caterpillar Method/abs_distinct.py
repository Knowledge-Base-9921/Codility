# Caterpillar Method / AbsDistinct

# Compute number of distinct absolute values of sorted array elements.

'''
A non-empty array A consisting of N numbers is given. The array is sorted in non-decreasing order. The absolute distinct count of this array is the number of distinct absolute values among the elements of the array.

For example, consider array A such that:

  A[0] = -5
  A[1] = -3
  A[2] = -1
  A[3] =  0
  A[4] =  3
  A[5] =  6
The absolute distinct count of this array is 5, because there are 5 distinct absolute values among the elements of this array, namely 0, 1, 3, 5 and 6.

Write a function:

def solution(A)

that, given a non-empty array A consisting of N numbers, returns absolute distinct count of array A.

For example, given array A such that:

  A[0] = -5
  A[1] = -3
  A[2] = -1
  A[3] =  0
  A[4] =  3
  A[5] =  6
the function should return 5, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−2,147,483,648..2,147,483,647];
array A is sorted in non-decreasing order.
'''

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Implement your solution here
    # Use a set to store unique absolute values.
    # Sets provide efficient (average O(1)) addition and membership testing,
    # and automatically handle uniqueness.
    distinct_abs_values = set()

    # Iterate through each element in the input array A.
    for x in A:
        # Calculate the absolute value of the current element.
        abs_x = abs(x)
        
        # Add the absolute value to the set.
        # If the value is already in the set, adding it again has no effect.
        distinct_abs_values.add(abs_x)
    
    # The number of distinct absolute values is simply the size of the set.
    return len(distinct_abs_values)
