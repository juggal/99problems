# Lotto: Draw N different random numbers from the set 1..M

from linked_list.sll import sll
import random


def rnd_select(ll, n):
    """
    Extract a number of randomly selected 
    elements from given linked list

    Parameters
    __________
    ll: sll
        linked list on which to be operated on
    n: int
        number of elements to randomly select

    Returns
    _______
    sll
        linked list containing randomly selected elements
    """
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
    """
    Generate a linked list of all integers in given range

    Parameters
    __________
    start: int
        starting integer in range of elements
    end: int
        ending integer in range of elements

    Returns
    _______
    sll
        linked list containing all integers of given range
    """
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
    """
    Extract N random numbers selected from 
    linked list containing elements from 1..M

    Parameters
    __________
    m: int
       upper limit of range till where to generate the linked list
    n: int
        number of elements to randomly select

    Returns
    _______
    sll
        linked list of randomly select elements in range 1 to m
    """
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
