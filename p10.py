# Run-length encoding of a list.

from linked_list.sll import sll


def encode(ll):
    """
    Apply run length encoding on given linked list

    Parameters
    __________
    ll: sll
        linked list on which to be operated on

    Returns
    _______
    str
        view of run length encoded linked list
    """
    curr = ll.head
    prev = curr.data
    result = "(("
    count = 0

    while curr != None:
        if prev == curr.data:
            count += 1
        else:
            result += str(count) + " " + str(prev) + ") ("
            prev = curr.data
            count = 1

        curr = curr.link
    result += str(count) + " " + str(prev) + "))"

    return result


def main():
    values = input("Enter elements:").split()
    ll = sll()
    for elem in values:
        ll.insert(elem)

    print(encode(ll))


if __name__ == "__main__":
    main()
