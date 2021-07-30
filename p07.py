# Flatten a nested list structure.

values = ['a', 'b', ['c', 'd', ['e', 'f']], 'g']

""" Going through each element recursively
if encountered element is list returning each elements of nested lists recursively 
else just returning element """


def flatten(temp_list):
    if len(temp_list) == 0:
        return temp_list
    if isinstance(temp_list[0], list):
        return flatten(temp_list[0]) + flatten(temp_list[1:])
    else:
        return temp_list[:1] + flatten(temp_list[1:])


flatten_values = flatten(values)
print(flatten_values)
