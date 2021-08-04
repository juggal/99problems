# Find the K'th element of a list
from linked_list.sll import sll


def element_at(ll, position):
    """
    Get the element at specified position

    Parameters
    _________
    ll: sll
        linked list on which to be operated on
    position: int
        position of element in linked list

    Returns
    _______
    any
        Element found at specified position
    """
    curr = ll.head
    i = 1
    while curr != None:
        if i == position:
            break
        i += 1
        curr = curr.link

    if curr == None:
        return "Index out of range"
    else:
        return curr.data


def main():
    values = input("Enter elements:").split()
    pos = int(input("Position:"))
    ll = sll()

    for elem in values:
        ll.insert(elem)

    result = element_at(ll, pos)
    print(result)


if __name__ == "__main__":
    main()
