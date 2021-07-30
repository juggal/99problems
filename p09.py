# Pack consecutive duplicates of list elements into sublists.

values = input("Enter elements:").split()
encoded_values = []

temp = [values[0]]
for elem in values[1:]:
    if elem in temp:
        temp.append(elem)
    else:
        encoded_values.append(temp)
        temp = [elem]

encoded_values.append(temp)


print(encoded_values)
