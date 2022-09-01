# Handy string-manipulator functions:
import re
from string import printable
from random import shuffle

numbers = printable[:10]
symbols = printable[62:]

# Get sub-string contained within brackets in text
str_in_bracs = lambda s: re.search(r"\(([A-Za-z0-9_]+)\)", s)

# Keep only alphabets inside text
keep_letters = lambda s: ''.join(filter(lambda x: x.isalpha(), s))

# Total count of characters in your string/text (optional: exclude="word/character")
chr_count = lambda text, exclude=[]: len(mreplace(text, exclude)) if exclude else len(text)

# Convert a string to in an alternating upper and lower case fashion
def altercaps(s, capstart=True): 
    # capstart = True -> First character as upper-case, followed by alternating caps for the next chrs.
    if startcap:
        return ''.join([chr.upper() if i%2 else chr.lower() for i, chr in enumerate(s, 1)])
    return ''.join([chr.upper() if not i%2 else chr.lower() for i, chr in enumerate(s, 1)])


# Multi-replace: Replace multiple sub-strings within a string
def mreplace(text, to_replace):
    # to_replace = dict -> {old_text : new_text, ...}
    if to_replace:
        if isinstance(to_replace, str):
            to_replace = {item:'' for item in to_replace.split()}
                
        # If "to_replace" passed as a list/tuple/set/str,
        # remove these items within the text automatically.
        if isinstance(to_replace, (list, tuple, set)): 
            to_replace = {item:'' for item in to_replace}

        for old, new in to_replace.items(): #Replace all substrings
            text = text.replace(old, new) #with new vals
        
    return text


# Get counts of unique sub-strings/words in a string
def word_count(text, exclude=[]):
    counts = {}
    
    if exclude:
        text = mreplace(text, exclude)
        
    for word in text.split():
        if word in counts.keys():
            counts[word] += 1
        else:
            counts[word] = 1

    return counts


# Collect and/or count sentences from strings/text.
def sentences(text, aslist=False, count=True, exclude=[]):
    sents, result = [], None
    
    if exclude:
        text = mreplace(text, exclude)
    
    for i in text.split('.'):
        i = i.strip()
        for j in i.split('?'):
            j = j.strip()
            for k in j.split('!'):
                k = k.strip()
                sents.append(k)
        if i == '':
            break
    
    # Return type
    if count and aslist:
        result = {'count':len(sents), 'sentences':sents}
    elif count: 
        result = len(sents)
    elif aslist:
        result = sents

    return result


# Collect and/or count paragraphs from strings/text.
def paragraphs(text, aslist=False, count=True, exclude=[]):
    paras = text.split('\n') # Starting example for the work, to be continued...
    
    # Return type
    if count and aslist:
        result = {'count':len(paras), 'paras':paras}
    elif count: 
        result = len(paras)
    elif aslist:
        result = paras
        
    return result


# Get random string of "n" number of characters (or n-sized string)
def randchr(n=len(printable), join=''):
    chrs = list(printable)
    shuffle(chrs)

    return join.join(chrs)[:n+1]

# Shuffle a string's word-positions and/or each word's characters
def str_shuffle(x, words=True, chrs=False):
    
    word_list = x.split()
    
    if words:
        shuffle(word_list)
    
    if chrs:
        for i in range(len(word_list)):
            word_letters = word_list[i].split()
            shuffle(word_letters)
            word_list[i] = ''.join(word_letters)
    
    return ' '.join(word_list)
    

# Sort a string based on by all characters (or words) alphabetically
def str_sort(x, by='w', reverse=False):
    by_format = by.lower().strip()
    xtype = type(x)
    
    if not isinstance(x, str):
        raise TypeError(f"Invalid {xtype} input, only strings/text allowed (enclosed within \"\" or '' quotation marks).")
    
    if by_format in {'w','word','words'}:
        return ' '.join(sorted(x.split(), reverse=reverse))
    
    elif by_format in {'c','chr','chrs', 'character', 'characters'}:
        return ''.join(sorted(x), reverse=reverse)
    
    raise ValueError(f"Invalid 'by' input, only valid options are in word format (by='w'/'word'/'words')\n"+
                     "or character format (by='c'/'chr'/'chrs'/'character'/'characters')")


# Convert strings to their ordinal form.
def ordinal(x, as_str=True):
    if as_str:
        joiner = as_str if isinstance(as_str, str) else ''
        id_list = joiner.join([str(ord(i)) for i in x if isinstance(i, str)])
    else:
        id_list = [ord(i) for i in x if isinstance(i, str)]
        
    return id_list

# Return an encrypted string with it's decription-keys
# def encrypt(x): # Working on it, TBC...
    
