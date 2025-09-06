# Stack and Queue / Brackets

# Determine whether a given string of parentheses (multiple types) is properly nested.

'''
A string S consisting of N characters is considered to be properly nested if any of the following conditions is true:

S is empty;
S has the form "(U)" or "[U]" or "{U}" where U is a properly nested string;
S has the form "VW" where V and W are properly nested strings.
For example, the string "{[()()]}" is properly nested but "([)()]" is not.

Write a function:

def solution(S)

that, given a string S consisting of N characters, returns 1 if S is properly nested and 0 otherwise.

For example, given S = "{[()()]}", the function should return 1 and given S = "([)()]", the function should return 0, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..200,000];
string S is made only of the following characters: '(', '{', '[', ']', '}' and/or ')'.
'''

def solution(S):

    _stack = []

    # Key: Closing value, Value: Opening value
    bracket_map = {
        ")":"(",
        "]":"[",
        "}":"{"
    }

    for c in S:
        # If character is an opening value
        if c in bracket_map.values():
            _stack.append(c)
        # If character is a closing value
        elif c in bracket_map.keys():
            # If stack is empty
            if not _stack:
                return 0
            
            _top_c = _stack.pop()

            if bracket_map[c] != _top_c:
                return 0
            
    return 1 if not _stack else 0