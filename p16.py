# Drop every N'th element from a list

values = input("Enter elements:").split()
n = int(input("N:"))
new_values = []

i = 0
while i < len(values):
    if (i + 1) % n != 0:
        new_values.append(values[i])
    i += 1

print(new_values)
