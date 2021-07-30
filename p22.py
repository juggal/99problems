# Create a list containing all integers within a given range

start = int(input("Start:"))
end = int(input("End:"))


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


print(gen_range(start, end))
