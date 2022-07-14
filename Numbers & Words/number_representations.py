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
    # num2words(2012345007) returns: 
    # "Reading 2,012,345,007 as:
    #  two billion, twelve million, three-hundred and fourty-five thousand, and seven"

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
        if type(x) != int:
            x = int(x)

        strx = str(x) # X as a string
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

    # ------------- "Main" of our function -------------
    x = f'{num:,}' # Python < 3.6: "{:,}".format(num)
    commas_left = x.count(',') # Number of commas in our number
    chunks_left = x.count(',') + 1 # Number of digit-chunks between commas
    sep = f' {sep.strip()} '

    num_words = [] # old: = ', '.join(map(less_than_1k, x.split(',')))
    
    for tri_digits in x.split(','):

        # Chunk's expression (Billion/Million/thousand/etc)
        expr = ' '+ten_to_3n[commas_left] 
        
        # If chunk is not "000" (or = 0)
        not_empty_chunk = int(tri_digits)

        if not_empty_chunk: 
            chunks_left -= 1 # Next digit-chunks left to loop over
            
            chunk2words = less_than_1k(tri_digits, expr = expr)

            # Add seperator to the expression of the last chunk
            # that contains only 1 or 2 digits
            if not_empty_chunk < 100 and not chunks_left:
                chunk2words = sep.lstrip() + chunk2words 
            
            num_words.append(chunk2words) # words collected for chunk
            
            commas_left-=1
        else:
            # Skip commas/empty-chunks ('000' or 0)
            commas_left -= 1
            chunks_left -= 1
        
    # "Confirm" to show our comma-separated number.
    if confirm:
        print('Reading',x,'as:')

    return ', '.join(num_words)
