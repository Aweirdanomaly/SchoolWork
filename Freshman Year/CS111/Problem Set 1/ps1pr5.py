# 
# ps1pr5.py - Problem Set 1, Problem 5

def first_and_last(values):
    """ takes first and last elements from list and concatenates them """
    first = values[0]
    last = values[-1]
    return [first, last]


def longer_len(s1, s2):
    """ takes two strings and returns the length of the longest one"""
    if len(s1) < len(s2):
        return (len(s2))
    else:
        return (len(s1))
        
    
def move_to_end(s, n):
    """takes in string "s" and integer "n" and moves 
    the first "n" characters to the end of the string"""
    if n >= len(s) :
        return (s)
    else:
        s = s[n:] + s[0:n]
        return (s)
   