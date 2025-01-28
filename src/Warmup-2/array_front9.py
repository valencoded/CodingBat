"""
Given an array of ints, return True if one of the first 4 elements in the array is a 9. The array length may be less than 4.
"""
def array_front9(arr):
    count = 0
    for i in range(len(arr)):
        if count == 4:
            break
        if arr[i] == 9:
            return True
        count += 1
    return False