# Lotto: Draw N different random numbers from the set 1..M

from linked_list.sll import sll
import random


def rnd_select(ll, n):
    curr = ll.head
    stack = []
    temp_list = sll()

    i = 1
    while i <= n:
        stack.append(random.randint(1, ll.get_length()))
        i += 1

    i = 1
    while i <= n:
        elem = ll.get_element(stack.pop())
        temp_list.insert(elem)
        i += 1

    return temp_list


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


def lotto_select(m, n):
    ll = gen_range(1, m)
    temp_list = rnd_select(ll, n)

    return temp_list


def main():
    m = int(input("Enter M:"))
    n = int(input("Enter N:"))

    lotto_list = lotto_select(m, n)
    lotto_list.display()


if __name__ == "__main__":
    main()
