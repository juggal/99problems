# Replicate the elements of a list a given number of times

values = input("Enter elements:").split()
repeat = int(input("No of time to replicate:"))
duplicate_values = []

for elem in values:
    for i in range(repeat):
        duplicate_values.append(elem)

print(duplicate_values)
