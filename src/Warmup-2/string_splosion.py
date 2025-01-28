"""
Given a non-empty string like "Code" return a string like "CCoCodCode".
"""
def string_splosion(str):
    word = ""
    for i in range(len(str)):
        word = word + str[:i+1]
    return word