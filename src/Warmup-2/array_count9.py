"""
Given an array of ints, return the number of 9's in the array.
"""
def array_count9(arr):
    count = 0
    for i in range(len(arr)):
        if arr[i] == 9:
            count += 1
    return count