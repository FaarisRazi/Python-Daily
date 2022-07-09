
# Retrieve unique lists/tuples from a nested-list (eg; [[1,2], [2,1]] => [1,2])
unique_lists = lambda nested_list: list(set([tuple(sorted(i)) for i in nested_list]))
