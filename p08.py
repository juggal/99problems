# Eliminate consecutive duplicates of list elements.

values = input("Enter elements:").split()
de_duplicate = []

"""Go through each element of input list iteratively if it does not exist in new list push the element"""
for elem in values:
    if elem not in de_duplicate:
        de_duplicate.append(elem)

print(de_duplicate)
