# Find the number of elements of a list

from linked_list.sll import sll


def count_elements(ll):
    """
    calculate length of linked list

    Parameters
    ----------
    ll: sll
        linked list on which to be operated on

    Returns
    -------
    int
        length of linked list
    """
    curr = ll.head
    length = 1
    while curr.link != None:
        length += 1
        curr = curr.link

    return length


def main():
    values = input("Enter elements:").split()
    ll = sll()

    for elem in values:
        ll.insert(elem)

    result = count_elements(ll)
    print(result)


if __name__ == "__main__":
    main()
