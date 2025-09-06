# Stack and Queue / StoneWall

# Cover "Manhattan skyline" using the minimum number of rectangles.

'''
You are going to build a stone wall. The wall should be straight and N meters long, and its thickness should be constant; however, it should have different heights in different places. The height of the wall is specified by an array H of N positive integers. H[I] is the height of the wall from I to I+1 meters to the right of its left end. In particular, H[0] is the height of the wall's left end and H[N−1] is the height of the wall's right end.

The wall should be built of cuboid stone blocks (that is, all sides of such blocks are rectangular). Your task is to compute the minimum number of blocks needed to build the wall.

Write a function:

def solution(H)

that, given an array H of N positive integers specifying the height of the wall, returns the minimum number of blocks needed to build it.

For example, given array H containing N = 9 integers:

  H[0] = 8    H[1] = 8    H[2] = 5
  H[3] = 7    H[4] = 9    H[5] = 8
  H[6] = 7    H[7] = 4    H[8] = 8
the function should return 7. The figure shows one possible arrangement of seven blocks.



Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array H is an integer within the range [1..1,000,000,000].
'''

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(H):
    # Implement your solution here
    _stack = []

    blocks_count = 0

    for height in H:
        # While the stack is not empty AND the current building's height
        # is less than the height of the block at the top of the stack:
        # This means the block at the top of the stack has ended, as we've
        # moved to a shorter building. We pop it because it's no longer relevant
        # for covering the current or subsequent buildings at this height.
        while _stack and height < _stack[-1]:
            _stack.pop()

        # If the stack is empty OR the current building's height is greater than
        # the height of the block at the top of the stack:
        # This indicates that we need to start a new block (rectangle)
        # to cover the current building. This new block will extend
        # from the current position up to the 'height'.
        # We push this new height onto the stack.
        if not _stack or height > _stack[-1]:
            _stack.append(height)
            blocks_count += 1

    return blocks_count