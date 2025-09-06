# Fibonacci Numbers / Sum of two Fibonacci numbers

'''
For all the given numbers x0, x1, . . . , xn−1, such that 1 <= xi <= m <= 1 000 000,
check whether they may be presented as the sum of two Fibonacci numbers
'''

# O(n + m)

import math

def solution(X):
    """
    Checks for each number in array X whether it can be presented as the sum of two Fibonacci numbers.

    Args:
        X: A list of integers. Each element xi is such that 1 <= xi <= m <= 1,000,000.

    Returns:
        A list of booleans, where result[k] is True if X[k] can be represented
        as the sum of two Fibonacci numbers, and False otherwise.
    """
    
    # Step 1: Generate Fibonacci numbers up to a maximum value.
    # The maximum value for X[i] is 1,000,000.
    # We need Fibonacci numbers up to this value.
    # F(0) = 0, F(1) = 1, F(2) = 1, F(3) = 2, F(4) = 3, F(5) = 5, ...
    # F(30) = 832040, F(31) = 1346269. So, we need up to F(30) or F(31) for sums.
    # The largest number we need to check is 1,000,000.
    # If a number is F_a + F_b, and F_a <= 1,000,000 and F_b <= 1,000,000,
    # then the sum can be up to 2,000,000.
    # However, the problem states xi <= 1,000,000.
    # So we need Fibonacci numbers up to 1,000,000.
    
    fib_numbers = set() # Use a set for O(1) average-case lookup
    fib_list = [0, 1]   # Start with F(0) and F(1)
    fib_numbers.add(0)
    fib_numbers.add(1)

    a, b = 0, 1
    while b <= 1000000: # Generate Fibonacci numbers up to the maximum possible input value
        next_fib = a + b
        if next_fib > 1000000: # Optimization: stop if the next Fibonacci number exceeds max X[i]
            break
        fib_list.append(next_fib)
        fib_numbers.add(next_fib)
        a = b
        b = next_fib

    # Step 2: For each number in the input array X, check if it's a sum of two Fibonacci numbers.
    results = []
    for num in X:
        found = False
        # Iterate through all generated Fibonacci numbers (as the first term)
        for fib1 in fib_list:
            # Calculate the required second Fibonacci number
            fib2_needed = num - fib1
            
            # Check if fib2_needed is also a Fibonacci number.
            # We also need to ensure fib2_needed is non-negative.
            if fib2_needed >= 0 and fib2_needed in fib_numbers:
                found = True
                break # Found a pair, no need to check further for this 'num'
        results.append(found)

    return results