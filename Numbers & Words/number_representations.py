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

def num2words(x):
    singles = dict(enumerate(['one','two','three','four',
                         'five','six','seven','eight','nine'],1))

    unique_tens = {10:'ten', 11:'eleven', 12:'twelve'}

    lvl2 = {20:'twenty', 30:'thirty', 40: 'fourty', 50:'fifty', 
            60:'sixty', 70:'seventy', 80:'eighty', 90:'ninety'}

    tens = {**unique_tens, 
            **{10+i//10:j[:-2]+'teen' for i,j in lvl2.items() if i > 20}}
    
    # To be continued ...
