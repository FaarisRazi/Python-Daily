
# How to present numbers with their as ordinal
def ordinal(num, include=True):
    str_num, suffix = f"{num}", 'th'

    if not 11 <= abs(num)%100 <= 13:
        suffix = {1:'st', 2:'nd', 3:'rd'}.get(num%10, 'th')
    
    if not include and include != '':
        return suffix

    if type(include) == str:
        str_num += include

    return str_num + suffix

    
