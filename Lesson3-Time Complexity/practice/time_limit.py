# Time Complexity / Time Limit

'''
n <= 1 000 000, the expected time complexity is O(n) or O(n log n),
n <= 10 000, the expected time complexity is O(n2),
n <= 500, the expected time complexity is O(n3).
'''

def count_numbers_linear(n):
    result = 0
    for i in range(1,n+1):
        result += i
    return result

def count_numbers_constant(n):
    result = (n * (n-1))/2
    return result