# Run-length encoding of a list.
values = input("Enter elements:").split()
encoded_values = []
temp1 = [values[0]]
temp2 = []

for elem in values[1:]:
    if elem in temp1:
        temp1.append(elem)
    else:
        temp2.append(temp1)
        temp1 = [elem]

temp2.append(temp1)

for elem in temp2:
    encoded_values.append([len(elem), elem[0]])

print(encoded_values)
