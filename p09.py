# Pack consecutive duplicates of list elements into sublists.

from linked_list.sll import sll


def pack(ll):
    """
    Packing duplicate elements into a sublist

    Parameters
    __________
    ll: sll
        linked list on which to be operated on

    Returns
    _______
    str
        view of packed duplicate elements into sublist
    """
    curr = ll.head
    prev = curr.data
    result = "(("

    while curr != None:
        if prev == curr.data:
            result += str(curr.data) + " "
        else:
            prev = curr.data
            result = result.strip(" ")
            result += ") (" + str(prev) + " "
        curr = curr.link
    result = result.strip(" ")
    result += "))"

    return result


def main():
    values = input("Enter elements:").split()
    ll = sll()
    for elem in values:
        ll.insert(elem)

    print(pack(ll))


if __name__ == "__main__":
    main()
