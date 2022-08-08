# Note: Data Structures will often be referred in short as "basket" in this script.

types = [list, tuple, set, dict, str]

# To check if an object/data is a data-structure (one of "types" above).
is_structure = lambda x: isinstance(x, types)

# Retrieve unique lists/tuples from a nested-list (eg; [[1,2], [2,1]] => [1,2]).
unique_lists = lambda nested_list: list(set([tuple(sorted(i)) for i in nested_list]))

# Sort a dictionary by it's keys (by="k") or values (by="v")
def sort_dict(x, by='k', reverse=False):
    sort_rule = {'k':0, 'v':1}
    return dict(sorted(x.items(), key=lambda x: x[sort_rule[by]], reverse=reverse))
    

# Flatten a data-structure of nested items.
def flatten(x):
    # Example lst = [[1], {2,3}, (4,5), 6, "seven"]:
    # flatten(lst) = [1, 2, 3, 4, 5, 6, 'seven']
    
    if not is_structure(x):
        raise ValueError(f"Invalide {basket} input, only data-structures"+
                          "\n(list, tuple, set, dict, str) allowed."  )
    basket = type(x)
    xlist = [list(i) if not isinstance(i, (int, float, str)) else [i] for i in x]

    return basket(sum(xlist, []))


# Split a data-structure's items to even-split (nested) chunks of items
import numpy as np
def even_chunks(basket, nchunks=2):
    basket_type = type(basket)
    inner = basket_type

    if isinstance(basket, set):
        inner = tuple
    
    elif isinstance(basket, str):
        basket_type = list
        basket = basket_type(basket)
        inner = basket_type

    chunked_up = np.array_split(basket, nchunks)
    
    return basket_type(map(inner, chunked_up))


# Make Ragged-Arrays
def ragged(basket=[], nests=5, start=0, stop=0, inner=list):
    # nests = int -> Number of "nests"/sub-lists inside our list/tuple/set
    # start = int -> Values in sub-lists to start counting from, examples:
    # stop = int (default: 0) -> Stop at an item/number > "start", within sub-lists.
    
    # Examples:
    # ragged(stop=7)            = [[0], [1, 2], [3, 4, 5], [6, 7]]
    # ragged(start=-4, nests=3) = [[-4], [-3, -2], [-1, 0, 1]]
    # ragged("Hello World")     = [['H'], ['e', 'l'], ['l', 'o', ' '], ['W', 'o', 'r', 'l'], ['d']]
    
    # ---------------------- Base-Case:
    if basket and isinstance(basket, types):
        ragged_map = dict(enumerate(basket))
        
        n_items = len(basket)
        basket = type(basket)
        ragged_keys = ragged(nests = n_items, stop = n_items-1)
        
        if basket == set: inner = tuple

        ragged_basket = [inner(map(ragged_map.get, sublst)) 
                                        for sublst in ragged_keys]
        return basket(ragged_basket)

    upto = nests
    lst, k = [], 0

    for i in range(1, upto+1):
        sublst = []

        for j in range(i):
            num = i+j+k
            item = start + num-1

            if item <= stop and stop > start:
                sublst.append(item)
        
        if sublst:
            lst.append(sublst)
        
        k = num-i
    
    return lst


# (Incomplete) Shuffle a basket of items and/or items within sub-baskets
# Thinking of including range-objects
def shuffle_basket(x, inner=False, outer=True):
    from random import shuffle
    basket = type(x)

    if outer:
        if basket == dict:
            x = x.items()
        x = list(x)
        
    shuffle(x)

    if inner:
        if basket == dict:
            for k,v in x.items():
                if isinstance(v, types):
                    x[k] = shuffle_basket(v)

        elif isinstance(x, types):
            x = list(x)
            
            for i in range(len(x)):
                item = x[i]

                if isinstance(item, types):
                    x[i] = shuffle_basket(item)
                    
    return basket(x)


# Get a random data-structure/"basket" (list/tuple.. etc) containing random characters/numbers.
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
    max_int = 9223372036854775807 # From sys.maxsize ('sys' library)
    
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
