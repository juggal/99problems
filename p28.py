# Sorting a list of lists according to length of sublists

values = [
    ['a', 'b', 'c'],
    ['d', 'e'],
    ['f', 'g', 'h'],
    ['d', 'e'],
    ['i', 'j', 'k', 'l'],
    ['m', 'n'],
    ['o']
]

# apply insertion sort on length of list elements


def lsort(nested_list):
    i = 1
    while i < len(nested_list):
        key = nested_list[i]
        j = i - 1
        while j >= 0:
            if len(key) < len(nested_list[j]):
                nested_list[j + 1] = nested_list[j]
                j -= 1
            else:
                break
        nested_list[j + 1] = key
        i += 1


lsort(values)
print(values)
