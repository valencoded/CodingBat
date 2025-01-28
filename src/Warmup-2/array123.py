"""
Given an array of ints, return True if the sequence of numbers 1, 2, 3 appears in the array somewhere.
"""
def array123(array):
    for i in range(len(array)-2):
        if array[i] == 1 and array[i+1] == 2 and array[i+2] == 3:
            return True
    return False