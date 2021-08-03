# Extract a given number of randomly selected elements from a list

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


def main():
    values = input("Enter elements:").split()
    n = int(input("Enter no of elements to select:"))
    ll = sll()

    for elem in values:
        ll.insert(elem)

    temp = rnd_select(ll, n)
    ll.display()
    temp.display()


if __name__ == "__main__":
    main()
