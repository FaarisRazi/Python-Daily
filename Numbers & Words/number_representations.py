
# Get ordinal numbers (eg; '1st', '2nd', '3rd', '10th', etc)
def ordinal(num, include=True):
    """
    include = True -> include number with suffix. (False -> return suffix). 
            = "str" -> include this string between the number and it's suffix.
    """
    str_num, suffix = f"{num}", 'th'
    # For < Python 3.6: str_num = "{}".format(num)

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
    
    return f'{num:,}' # For < Python 3.6: "{:,}".format(num)
