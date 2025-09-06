# Stack and Queue / Push Pop Function

'''
The stack can be represented by an array for storing the elements. Apart of the array, we
should also remember the size of the stack and we must be sure to declare sufficient space
for the array (in the following implementation we can store N elements)
'''

N = int(input("Enter N: "))
stack = [0] * N
size = 0

# O(1) -- Push

def push(x):
    global size
    stack[size] = x
    size += 1

# O(1) -- Pop

def pop():
    global size
    size -= 1
    return stack[size]