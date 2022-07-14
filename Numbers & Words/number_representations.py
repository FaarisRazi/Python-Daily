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


# Convert numbers to english-words (US) (Complete so far)
def num2words(num, sep='and', dec='point', show=True):
    # num2words(20145007.123) returns: 
    # "Reading 20,145,007.123 as:
    #  twenty million, one-hundred and fourty thousand, and seven, point one-two-three"
    
    # Formulating a Numbers-to-words dictionary:
    singles = dict(enumerate(['one','two','three','four',
                         'five','six','seven','eight','nine'],1))

    numtys = {20:'twenty', 30:'thirty', 40: 'fourty', 50:'fifty', 
              60:'sixty', 70:'seventy', 80:'eighty', 90:'ninety'}

    ten_teens = {10:'ten', 11:'eleven', 12:'twelve', 
                 **{i//10 + 10:j[:-2]+'teen' for i,j in numtys.items() if i > 20}}

    refdict = {**singles, **ten_teens, **numtys} # Main 'reference' dictionary to be used

    # Large-number names from - https://www.ibiblio.org/units/large.html
    ten_to_3n = dict(enumerate(['','thousand', 'million','billion','trillion','quadrillion',
                 'quintillion','sextillion','septillion','octillion','nonillion',
                 'quintilliard','undecillion','duodecillion','tredecillion',
                 'quattuordecillion','quindecillion','sexdecillion','septendecillion',
                 'octodecillion','novemdecillion','vigintillion','unvigintillion',
                 'duovigintillion','duodecillion','quattuorvigintillion','quinvigintillion',
                 'sexvigintillion','septenvigintillion','octovigintillion','quindecillion',
                 'trigintillion','untrigintillion','duotrigintillion']))

    def less_than_1k(x, expr='', just0='zero'):
        
        if not isinstance(x, int):
            x = int(x)

        strx = str(x) # X as a string
        n_digits = len(strx) # n-number of digits in X
        ten_factor = 10**(n_digits - 1) # 10^(n-1). (n = number of digits)
        fdigits = x % ten_factor # "final" digit/s of X (single or double digits)

        # print(fdigits) # To track recursions (next fdigits)
        if n_digits == 2:
            words = refdict[x] if x < 20 else refdict[x//10 * 10]
            words += '-'+refdict[fdigits] if x < 10 else ''
        
        elif n_digits == 3:
            base = refdict[x//ten_factor] +'-hundred'

            # Recursion for the last two digits, or repeat the above if-condition's chunk...
            words = base+' and '+less_than_1k(fdigits) if fdigits else base
        else:
            words = refdict[x] if x else just0

        return words + expr

    # ------------- "Main" of our function -------------
    decimals = ''
    x = f'{num:,}'                  # Python < 3.6: "{:,}".format(num)
    commas_left = x.count(',')      # Number of commas in our number
    chunks_left = commas_left + 1   # Number of digit-chunks between commas
    sep = f' '+sep.strip()+' '      # Separator with spaces
    
    num_words = [] # before: = ', '.join(map(less_than_1k, x.split(',')))
    
    # Dealing with decimal/float numbers:
    if isinstance(num, float):
        x, decimal_digits = x.split('.')

        if not num.is_integer():
            # Converting decimals to words
            decimals = '-'.join(map(less_than_1k, decimal_digits))

    # If our number is less than 4-digits
    if not commas_left: # or num < 1000
        num_words = less_than_1k(num)

    else:
        for tri_digits in x.split(','):

            # Chunk's expression (Billion/Million/thousand/etc)
            expr = ' '+ten_to_3n[commas_left] 
            
            # If chunk is not "000" (or = 0)
            not_empty_chunk = int(tri_digits)

            if not_empty_chunk: 
                chunks_left -= 1 # Next digit-chunks left to loop over
                
                chunk2words = less_than_1k(tri_digits, expr = expr).rstrip()

                # Add seperator to the expression of the last chunk
                # that contains only 1 or 2 digits
                if not_empty_chunk < 100 and not chunks_left:
                    chunk2words = sep.lstrip() + chunk2words 
                
                num_words.append(chunk2words) # words collected for chunk
                
                commas_left-=1 # Next commas left
            else:
                # Skip commas/empty-chunks ('000' or 0)
                commas_left -= 1
                chunks_left -= 1

        num_words = ', '.join(num_words)

    if decimals:
        dec = ', '+dec.strip()+' '
        num_words += dec + decimals

    # "show" -> to show our comma-separated number with result.
    if show:
        comment = 'Reading '+f'{num:,}'+' as:\t' + num_words
        print(comment.replace('\t','\n') if num > 99 else comment)

    return num_words
