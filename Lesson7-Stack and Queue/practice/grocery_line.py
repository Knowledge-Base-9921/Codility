# Stack and Queue / Grocery Line

'''
You are given a zero-indexed array A consisting of n integers: a0, a1, . . . , an-1.
Array A represents a scenario in a grocery store, and contains only 0s and/or 1s:
• 0 represents the action of a new person joining the line in the grocery store,
• 1 represents the action of the person at the front of the queue being served and leaving
the line.
The goal is to count the minimum number of people who should have been in the line before
the above scenario, so that the scenario is possible (it is not possible to serve a person if the
line is empty).
'''

def grocery_store(A):
    n = len(A)
    size, result = 0,0

    for i in range(n):
        if A[i] == 0:
            size += 1
        else:
            size -= 1
            result = max(result, -size) # if size is negative, deficit: more people moved from the line than added
    
    return result