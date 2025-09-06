# Stack and Queue / Queue

'''
The queue can be represented by an array for storing the elements. Apart of the array, we
should also remember the front (head) and back (tail) of the queue. We must be sure to
declare sufficient space for the array (in the following implementation we can store N - 1
elements).
'''

N = int(input("Enter N: "))
queue = [0] * N
head, tail = 0,0

# O(1) -- Push

def push(x):
    global tail
    tail = (tail + 1)%N
    queue[tail] = x

# O(1) -- Pop

def pop():
    global head
    head = (head + 1)%N
    return queue[head]

# O(1) -- Size

def size():
    return (tail - head + N) % N

# O(1) -- Empty

def empty():
    return head == tail