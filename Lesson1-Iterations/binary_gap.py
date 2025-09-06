# Iterations / Binary Gap

# Find longest sequence of zeros in binary representation of an integer.

'''
A binary gap within a positive integer N is any maximal sequence of consecutive zeros that is surrounded by ones at both ends in the binary representation of N.
For example, number 9 has binary representation 1001 and contains a binary gap of length 2. The number 529 has binary representation 1000010001 and contains two binary gaps: one of length 4 and one of length 3. The number 20 has binary representation 10100 and contains one binary gap of length 1. The number 15 has binary representation 1111 and has no binary gaps. The number 32 has binary representation 100000 and has no binary gaps.

Write a function: 'def solution(N)' that, given a positive integer N, returns the length of its longest binary gap. The function should return 0 if N doesn't contain a binary gap.
For example, given N = 1041 the function should return 5, because N has binary representation 10000010001 and so its longest binary gap is of length 5. Given N = 32 the function should return 0, because N has binary representation '100000' and thus no binary gaps.
Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..2,147,483,647].
'''

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def dec2bin(N:int):
    _binary = ""
    _temp_N = N

    while _temp_N > 0:
        _rem = _temp_N % 2
        _binary = str(_rem) + _binary
        _temp_N //= 2

    return _binary

def sliding_window(_binary:str):
    _max_result, _curr_result = 0,0

    for i in _binary:
        if i=='0':
            _curr_result+=1
        else: # RESET Condition
            _max_result = max(_max_result, _curr_result)
            _curr_result = 0

    return _max_result 

def solution(N):
    # Implement your solution here
    _binary = dec2bin(N)
    return sliding_window(_binary)

# Testing
n = int(input("Enter n: ")) # 529 = 1000010001
print(solution(n))
