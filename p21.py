# Insert an element at a given position into a list

values = input("Enter elements:").split()
new_value = input("New element:")
pos = int(input("Position:"))

updated_values = values[:pos - 1] + [new_value] + values[pos - 1:]

print(updated_values)
