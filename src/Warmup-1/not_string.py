"""
Given a string, return a new string where "not " has been added to the front.
However, if the string already begins with "not", return the string unchanged.
"""
def not_string(string):
    if(string[:3]=="not"):
        return string
    else:
        return "not " + string