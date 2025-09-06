# Prime and Composite Numbers / Reversing Coins

'''
Consider n coins aligned in a row. Each coin is showing heads at the beginning.
1 2 3 4 5 6 7 8 9 10
Then, n people turn over corresponding coins as follows. Person i reverses coins with numbers
that are multiples of i. That is, person i flips coins i, 2 · i, 3 · i, . . . until no more appropriate
coins remain. The goal is to count the number of coins showing tails. In the above example,
the final configuration is:
1 2 3 4 5 6 7 8 9 10
'''

# O(Nlog(N))

def coins(n):
    result = 0
    coin = [0] * (n+1)

    for i in range(1, n+1):
        j = i

        while(j <= n):
            coin[j] = (coin[j]+1)%2
            j+=1

        result += coin[i]

    return result