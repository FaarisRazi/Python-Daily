# Handy string-manipulator functions:

# Multi-replace: Replace multiple sub-strings within a string
def mreplace(text, to_replace):
    # to_replace = dict -> {text_to_replace : new_text, ...}
    
    # If items-to-replace passed as a list, these items
    # will automatically be removed from text.
    if type(to_replace) == list: 
        to_replace = {item:'' for item in to_replace}
        
    for old, new in to_replace.items(): #Replace all substrings
        text = text.replace(old, new) #with new vals
        
    return text

#Get sub-string contained within brackets in text
str_in_bracs = lambda s: re.search(r"\(([A-Za-z0-9_]+)\)", s)
