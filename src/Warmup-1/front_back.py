"""
Given a string, return a new string where the first and last chars have been exchanged.
"""
def front_back(string):
    if len(string) <= 1:
        return string
    first = string[0]
    last = string[-1]
    return last + string[1:-1] + first