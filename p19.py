# Rotate a list N places to the left

values = input("Enter elements:").split()
n = int(input("N:"))

shifted_values = values[n:] + values[:n]

# if n < 0:
#     n = len(values) + n
# temp1 = []
# temp2 = []

# for idx, elem in enumerate(values):
#     if (idx + 1) <= n:
#         temp1.append(elem)
#     else:
#         temp2.append(elem)

# shifted_values = temp2 + temp1

print(shifted_values)
