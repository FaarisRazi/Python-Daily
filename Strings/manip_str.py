# Handy string-manipulator functions:
import re
from string import printable
from random import shuffle

numbers = printable[:10]
symbols = printable[62:]

# Get sub-string contained within brackets in text
str_in_bracs = lambda s: re.search(r"\(([A-Za-z0-9_]+)\)", s)

# Keep only alphabets inside text
only_letters = lambda s: ''.join(filter(lambda x: x.isalpha(), s))

# Convert a string to in an alternating upper and lower case fashion
def altercaps(s, capstart=True): 
    # capstart = True you want to start your string as upper-case, followed then by alternating caps.
    if startcap:
        return ''.join([chr.upper() if i%2 else chr.lower() for i, chr in enumerate(s, 1)])
    return ''.join([chr.upper() if not i%2 else chr.lower() for i, chr in enumerate(s, 1)])


# Multi-replace: Replace multiple sub-strings within a string
def mreplace(text, to_replace):
    # to_replace = dict -> {old_text : new_text, ...}
    
    # If "to_replace" passed as a list/tuple/set/str,
    # remove these items within the text automatically.
    if isinstance(to_replace, (list, tuple, set)): 
        to_replace = {item:'' for item in to_replace}
        
    for old, new in to_replace.items(): #Replace all substrings
        text = text.replace(old, new) #with new vals
        
    return text


# Get counts of unique sub-strings/words in a string
def word_counts(text):
    counts = {}

    for word in text.split():
        if word in counts.keys():
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

# Get random string of "n" number of characters (or n-sized string)
def randchr(n=len(printable), join=''):
    chrs = list(printable)
    shuffle(chrs)

    return join.join(chrs)[:n+1]
