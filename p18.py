# Extract a slice from a list

values = input("Enter elements:").split()
i = int(input("I:"))
k = int(input("K:"))

slice_values = [values[idx] for idx in range(i - 1, k)]

print(slice_values)
