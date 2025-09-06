# Prime and Composite Numbers / Mini Perimeter Rectangle

# Find the minimal perimeter of any rectangle whose area equals N.

'''
An integer N is given, representing the area of some rectangle.

The area of a rectangle whose sides are of length A and B is A * B, and the perimeter is 2 * (A + B).

The goal is to find the minimal perimeter of any rectangle whose area equals N. The sides of this rectangle should be only integers.

For example, given integer N = 30, rectangles of area 30 are:

(1, 30), with a perimeter of 62,
(2, 15), with a perimeter of 34,
(3, 10), with a perimeter of 26,
(5, 6), with a perimeter of 22.
Write a function:

def solution(N)

that, given an integer N, returns the minimal perimeter of any rectangle whose area is exactly equal to N.

For example, given an integer N = 30, the function should return 22, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..1,000,000,000].
'''

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    # Implement your solution here
    # Initialize minimum_perimeter to a very large number.
    # This ensures that any valid perimeter found will be smaller.
    minimum_perimeter = float('inf')
    
    # Iterate from 1 up to the square root of N.
    # We only need to check factors up to sqrt(N) because if 'i' is a factor,
    # then 'N // i' is also a factor, forming a pair of sides (i, N // i).
    # The pair closest to sqrt(N) will yield the minimum perimeter.
    i = 1
    while (i * i <= N):
        # Check if 'i' is a factor of N.
        if (N % i == 0):
            # If 'i' is a factor, then 'N // i' is its corresponding factor.
            # These two numbers can be the side lengths of a rectangle.
            side1 = i
            side2 = N // i
            
            # Calculate the perimeter for this pair of sides.
            current_perimeter = 2 * (side1 + side2)
            
            # Update the minimum_perimeter if the current_perimeter is smaller.
            minimum_perimeter = min(minimum_perimeter, current_perimeter)
        
        i += 1 # Move to the next potential factor

    return minimum_perimeter