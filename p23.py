# Extract a given number of randomly selected elements from a list

import random

values = input("Enter elements:").split()
n = int(input("No of values:"))

random_values = random.sample(values, n)

print(random_values)
