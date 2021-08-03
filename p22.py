# Create a list containing all integers within a given range

from linked_list.sll import sll, Node


def gen_range(start, end):
    ll = sll()

    if end < start:
        i = start
        while i >= end:
            ll.insert(i)
            i -= 1

    else:
        i = start
        while i <= end:
            ll.insert(i)
            i += 1

    return ll


def main():
    start = int(input("Start:"))
    end = int(input("End:"))

    ll = gen_range(start, end)
    ll.display()


if __name__ == "__main__":
    main()
