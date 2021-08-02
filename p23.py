# Extract a given number of randomly selected elements from a list

import random

values = input("Enter elements:").split()
n = int(input("No of values:"))

idx = [random.randint(0, (len(values) - 1)) for i in range(n)]

random_values = [values[i] for i in idx]
# random_values = random.sample(values, 3)

print(random_values)
