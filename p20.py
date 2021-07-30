# Remove the K'th element from a list

values = input("Enter elements:").split()
k = int(input("K:"))

new_values = values[:k - 1] + values[k:]
print(new_values)
