# Split a list into two parts; the length of the first part is given

values = input("Enter elements:").split()
n = int(input("N:"))

temp1 = []
temp2 = []

for idx, elem in enumerate(values):
    if (idx + 1) <= n:
        temp1.append(elem)
    else:
        temp2.append(elem)

split_values = [temp1, temp2]

print(split_values)
