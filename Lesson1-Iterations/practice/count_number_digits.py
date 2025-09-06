# Iterations / Count the number of digits

'''
Given a positive integer n, how can we count the number of digits in its decimal
representation? One way to do it is convert the integer into a string and count the characters.
Here, though, we will use only arithmetical operations instead. We can simply keep dividing
the number by ten and count how many steps are needed to obtain 0.
'''

n = int(input("Enter n: ")) # z.B., n=12345, result -> 5
temp_n = n

result = 0
while temp_n > 0:
    temp_n //= 10 # Do not confuse this with / as the type changes to float
    # print(temp_n)
    result+=1

print(f"{n} has {result} number of digits in its decimal place.")