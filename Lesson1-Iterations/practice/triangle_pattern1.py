# Iterations / Triangle Pattern 1

'''
Let’s print a triangle made of asterisks (‘*’) separated by spaces. The triangle
should consist of n rows, where n is a given positive integer, and consecutive rows should
contain 1, 2, . . . , n asterisks. For example, for n = 4 the triangle should appear as follows:
*
* *
* * *
* * * *
'''

n = int(input("Enter n: "))

for i in range(1,n+1):
    result = ""
    for j in range(i):
        result += "*"
    print(result)