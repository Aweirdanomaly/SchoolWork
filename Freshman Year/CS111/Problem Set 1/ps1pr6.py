# 
# ps1pr6.py - Problem Set 1, Problem 6

def mirror(s):
    """takes a string input and returns the
    same string plus itself backwards"""
    return(s + s[-1::-1])
    
def is_mirror(s):
    """checks if input string could've been produced by 'def mirror(s)' """
    w = len(s) // 2 
    if s[0:w] == s[-1:w-1:-1]:
        return True
    else:
        return False

def replace_end(values, new_end_vals):
    """replaces the last n values of the list 'values' with n values from 
    'new_end_vals' where n equals len(new_end_vals)"""
    n = len(new_end_vals)
    o = len(values)
    if n >= o:
        return (new_end_vals)
    else:
        values = values[0:o-n] + new_end_vals
        return values
    
    
def repeat_elem(values, index, num_times):
    """ takes the list values and concatenates a certain index in the list
    "values" "num_times" times"""
    rep = ( values[index:index+1] * num_times)
    list_end = values[index+1::1]
    values = values[0:index]  
    return(values + rep + list_end)