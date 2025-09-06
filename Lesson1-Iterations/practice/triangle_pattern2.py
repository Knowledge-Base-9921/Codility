# Iterations / Triangle Pattern 2

'''
Let’s print a triangle made of asterisks (‘*’) separated by spaces and consisting
of n rows again, but this time upside down, and make it symmetrical. Consecutive rows should
contain 2n − 1, 2n − 3, . . . , 3, 1 asterisks and should be indented by 0, 2, 4, . . . , 2(n − 1)
spaces. For example, for n = 4 the triangle should appear as follows:

* * * * * * * --> 0 + 7 + 0 = 7
X * * * * * X --> 1 + 5 + 1 = 7
X X * * * X X --> 2 + 3 + 2 = 7
X X X * X X X --> 3 + 1 + 3 = 7

'''

n = int(input("Enter n: "))

for i in range(n):
    result = ""

    # Left Space
    for j in range(i):
        result += " "

    # Asterisks
    for j in range(2*(n-i)-1):
        result += "*"

    # Right Space
    for j in range(i):
        result += " "
    
    print(result)