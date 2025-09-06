# Caterpillar Method / Caterpillar Method

'''
The Caterpillar method is a likeable name for a popular means of solving algorithmic tasks.
The idea is to check elements in a way that’s reminiscent of movements of a caterpillar.
The caterpillar crawls through the array. We remember the front and back positions of the
caterpillar, and at every step either of them is moved forward.

• if we can, we move the right end (front) forward and increase the size of the caterpillar;
• otherwise, we move the left end (back) forward and decrease the size of the caterpillar.

'''

# O(N)

def caterpillar_method(A, s):
    n = len(A)

    front, total = 0,0

    for back in range(n):
        while (front < n) and (total + A[front] <= s):
            total += A[front]
            front += 1
        
        if total == s:
            return True
        
        total -= A[back]

    return False