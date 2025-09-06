# Stack and Queue / Nesting

# Determine whether a given string of parentheses (single type) is properly nested.

'''
A string S consisting of N characters is called properly nested if:

S is empty;
S has the form "(U)" where U is a properly nested string;
S has the form "VW" where V and W are properly nested strings.
For example, string "(()(())())" is properly nested but string "())" isn't.

Write a function:

def solution(S)

that, given a string S consisting of N characters, returns 1 if string S is properly nested and 0 otherwise.

For example, given S = "(()(())())", the function should return 1 and given S = "())", the function should return 0, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..1,000,000];
string S is made only of the characters '(' and/or ')'.
'''

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    # Implement your solution here
    _stack = []

    for c in S:
        # Case: Opening '('
        if c == "(":
            _stack.append(c)
        # Case: Close ')'
        elif c == ")":
            if not _stack:
                return 0

            _top = _stack.pop()

            if _top != "(":
                return 0

    
    return 1 if not _stack else 0
