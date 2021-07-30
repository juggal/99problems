# Duplicate the elements of a list

values = input("Enter elements:").split()
duplicate_values = []

for elem in values:
    duplicate_values.append(elem)
    duplicate_values.append(elem)

print(duplicate_values)
