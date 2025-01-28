"""
Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo".
"""
def string_bits(string):
    word = ""
    for i in range (len(string)):
        if i%2 == 0:
            word= word+string[i]
    return word