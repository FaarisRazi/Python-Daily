
# Retrieve unique lists/tuples from a nested-list (eg; [[1,2], [2,1]] => [1,2])
unique_lists = lambda nested_list: list(set([tuple(sorted(i)) for i in nested_list]))

# Get a random data-structure/"basket" (list/tuple.. etc) containing random characters/numbers
def rand_basket(items=5, basket=any, nest=0, nest_type=any):
    # items = int -> Number of items in your "basket"
    # basket = any/list/tuple/set/dict -> data-structure type of your basket or 'any' for any type
    # nest = (later)
    # nest_type = (later)
    from random import choice, randint, random
    from string import printable
    
    data_structures = {list, tuple, set, dict, str}
    str_inputs = {'list', 'tuple', 'set', 'dict', 'str'}
    random_chrs = list(printable)
    max_int = 7512061515276834201
    
    if basket in {any, 'any'}:
        basket = choice([list, tuple, set, dict])
    
    if basket in data_structures or basket in str_inputs:
        if type(basket) == str:
            basket = eval(basket)
        
        random_items = []
        for i in range(items):
            rand_str = ''.join([choice(random_chrs) for i in range(randint(1,10))])
            rand_float = choice([random()]+random_chrs)
            rand_int = randint(0, max_int)
            rand_key = choice([choice(random_chrs), rand_float, rand_int])
            
            if i%2 == choice([0,1]):
                rand_value = rand_str
            else: 
                rand_value = choice([random(), randint(0, max_int)])
           
            random_items.append([rand_key, rand_value])
    else:
        raise ValueError(f"Invalid {type(basket)} basket input, "+
               "\nchoose 'any' or from [list, tuple, set, dict]")
    if basket == dict:
        return dict(random_items)
    else:
        return basket(choice(i) for i in random_items)
