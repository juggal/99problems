# Run-length encoding of a list (direct solution)

values = input("Enter elements:").split()
encoded_values = []

temp = values[0]
count = 1
for elem in values[1:]:
    if elem == temp:
        count += 1
    else:
        if count == 1:
            encoded_values.append(temp)
        else:
            encoded_values.append([count, temp])
        temp = elem
        count = 1


if count == 1:
    encoded_values.append(temp)
else:
    encoded_values.append([count, temp])

print(encoded_values)
