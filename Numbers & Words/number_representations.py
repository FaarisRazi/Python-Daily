alphabets = "abcdefghijklmnopqrstuvwxyz"

# Get ordinal numbers (eg; '1st', '2nd', '3rd', '10th', etc)
def ordinal(num, include=True):
    """
    include = True -> include number with suffix. (False -> return suffix). 
            = "str" -> include this string between the number and it's suffix.
    """
    str_num, suffix = f"{num}", 'th'
    # Or (Python < 3.6): str_num = "{}".format(num)

    if not 11 <= abs(num)%100 <= 13:
        suffix = {1:'st', 2:'nd', 3:'rd'}.get(num%10, 'th')
    
    if not include and include != '':
        return suffix

    if type(include) == str:
        str_num += include

    return str_num + suffix


# Long numbers with commas (eg; "1,000" , "98,765,432", etc)
def commas(num, r=0):    
    # r = int -> round to 'r' decimal places
    num = float(f'%.{r}f'%(num))

    if num.is_integer():
        num = int(num)
    
    return f'{num:,}' # Or (Python < 3.6): "{:,}".format(num)


# Convert numbers to words via digits-to-string mapping,
# with given IDs-list (str_ids) of string-values to map to your number's digits
def map_str(x, str_ids = {}, join=''):
    # str_ids = {int, float : str ...} -> Numeric-key to user's string/character
    typeX_error = f"Invalid {type(x)} input, only numbers allowed as text or as is."
    typeIDs_error = f"Invalid {type(x)} as IDs container, only lists/strings/dictionaries allowed."
    lenID_error = "Invalid IDs-list, Count of IDs < Count of your number's unique digits."
    
    strx = str(x).strip()
    
    # ------- x: Number Validation
    if strx.isdigit():
        pass
    elif strx.replace('.','').isdigit():
        return '.'.join(map(map_str, strx.split('.'), str_ids, join))
    else:
        raise type_err
    
    # ------- IDs-list: Assign/Validation
    if not str_ids:
        alphabets = 'abcdefghijklmnopqrstuvwxyz'
        str_ids = dict(enumerate(alphabets, 1))
        
    elif type(str_ids) == dict:
        pass
    
    elif type(str_ids) in {list, str}:
#         str_ids = set(str_ids)
        n_digits = len(set(strx))
        n_ids = len(str_ids)
        
        if n_ids != n_digits:
            if n_ids < n_digits:
                raise lenID_error
                
            print(f"count of IDs ({n_ids}) > count of your number's unique digits ({n_digits})"+
                  f",\nusing the first {n_digits} digits from your IDs-list.")
            
            str_ids = {n:s for n,s in zip(strx, str_ids[:n_digits])}
    else: 
        raise typeIDs_error

    return join.join(map( str_ids.get, map(int, strx) ))

# Convert numbers to english-words (US) (To be continued further...)
def num2words(num, sep='and', confirm=True):

    def less_than_1k(x, expr='', just0='zero'):
        x = int(x) # X = Our number
        strx = str(x)

        n_digits = len(strx) # n-number of digits in X
        ten_factor = 10**(n_digits - 1) # 10^(n-1). (n = number of digits)
        fdigits = x % ten_factor # "final" digit/s of X (single or double digits)

        if n_digits == 2:
            # print(fdigits)
            words = refdict[x] if x < 20 else refdict[x//10 * 10]+'-'+refdict[fdigits]
        
        elif n_digits == 3:
            base = refdict[x//ten_factor] +'-hundred'

            # Recursion for the last two digits, or repeat the above if-condition's chunk...
            words = base+' and '+less_than_1k(fdigits) if fdigits else base
        
        else:
            words = refdict[x] if x else just0

        return words + expr

        # ~~~~~~~~~~~~~~~~~~~ Old work for less_than_1000(): ~~~~~~~~~~~~~~~~~~~~
        # is_3digits = (n_digits == 3) # if X has 3 digits (True/False)
        # edigit = x % 10 # end-digit (last digit of X)
        # base = refdict[x//ten_factor] +'-hundred and ' if is_3digits else refdict[x//10 * 10]
        
        # if not fdigits: # If x is a multiple of 10 or 100
        #     return base.replace(' and ','')
        
        # digit2 = fdigits // 10**(n_digits - 2) # 2nd-digit of our number X
        # base2 = refdict[fdigits] if fdigits < 20 else refdict[digit2 * 10]+'-'
        
        # base += base2.replace('-','') if not edigit else base2#+refdict[edigit]
        # print(base)
        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    x = f'{num:,}' # For Python < 3.6: "{:,}".format(20345678)
    commas_left = x.count(',')
    sep = f' {sep} '

    # num_words = ', '.join(map(less_than_1k, x.split(',')))
    num_words = []
    for tri_digits in x.split(','):
        chunk = " "+ten_to_3n[commas_left] # Millionth/thousandth/etc "chunk"
        commas_left -= 1

        chunk2words = less_than_1k(tri_digits, expr = chunk)

        num_words.append(chunk2words)

    if confirm:
        print('Converting our number',x,'to:')
        
    return ', '.join(num_words)
