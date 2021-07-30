# Decode a run-length encoded list

encoded_values = [[4, 'a'], 'b', [2, 'c'], [2, 'a'], 'd', [4, 'e']]
decoded_values = []

for elem in encoded_values:
    if isinstance(elem, list):
        temp = [elem[1] for i in range(elem[0])]
        decoded_values += temp
    else:
        decoded_values.append(elem)

print(decoded_values)
