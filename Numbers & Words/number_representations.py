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

def num2words(num, sep='and'):

    x = f'{num:,}' # For Python < 3.6: "{:,}".format(20345678)
    commas_left = x.count(',')
    sep = f' {sep} '

    # if not commas_left:
    # def less_than_thousand(x):

        #     if n_digits < 3:
        #         if comma_num < 20:
        #             comma_words = lvl_word.get(comma_num)
        #         else:
        #             if comma_num%10:
        #                 a, b = map(int, comma_str)
        #                 base = lvl_word.get(a*10)
        #                 last = singles.get(b)
        #                 comma_words = base +'-'+ last
        #             else:
        #                 comma_words = lvl_word.get(comma_num)
        #     else:
        #         a, b, c = map(int, comma_str)
        #         comma_words = singles.get(a) + '-' + lvl_word

        #         if b:
        #             comma_words += sep + digit_lvls[2].get(b*10)

        #         if c:    
        #             comma_words += '-' + singles.get(c)

    num_words = ''
    for i, comma_x in enumerate(x.split(',')):
        comma_num = int(comma_x)
        comma_str = str(comma_num)
        n_digits = len(comma_str)

        comma_words = ''
        lvl_word = digit_lvls.get(n_digits)
        if comma_num:
            if n_digits < 3:
                if comma_num < 20:
                    comma_words = lvl_word.get(comma_num)
                else:
                    if comma_num%10:
                        a, b = map(int, comma_str)
                        base = lvl_word.get(a*10)
                        last = singles.get(b)
                        comma_words = base +'-'+ last
                    else:
                        comma_words = lvl_word.get(comma_num)
            else:
                a, b, c = map(int, comma_str)
                comma_words = singles.get(a) + '-' + lvl_word

                if b:
                    comma_words += sep + digit_lvls[2].get(b*10)

                if c:    
                    comma_words += '-' + singles.get(c)
            
            if commas_left and comma_num:
                comma_words += ' '+ten_to_3n.get(commas_left) + ', '
                commas_left -= 1

            # if comma_x == x.count(',') and comma_num < 100:

        num_words += comma_words

    print('Converting',x,'to: ',num_words)
    return num_words
    
    # To be continued ...
