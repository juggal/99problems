# Lotto: Draw N different random numbers from the set 1..M

import random

M = int(input("M:"))
N = int(input("N:"))


def gen_range(start, end):
    values = []
    if end < start:
        i = start
        while i >= end:
            values.append(i)
            i -= 1
    else:
        i = start
        while i <= end:
            values.append(i)
            i += 1
    return values


values = gen_range(1, M)

idx = [random.randint(0, (len(values) - 1)) for i in range(N)]

random_values = [values[i] for i in idx]

print(random_values)
