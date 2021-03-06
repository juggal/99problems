# Eliminate consecutive duplicates of list elements.

from linked_list.sll import sll


def compress(ll):
    """
    Remove duplicate elements from given linked list

    Parameters
    ----------
    ll: sll
        linked list on which to be operated on

    Returns
    -------
    None
    """
    curr = ll.head
    prev = curr

    while curr.link != None:
        if prev.data != curr.data:
            prev.link = curr
            prev = curr
        curr = curr.link

    if prev.data == curr.data:
        prev.link = None


def main():
    values = input("Enter elements:").split()
    ll = sll()
    for elem in values:
        ll.insert(elem)

    compress(ll)
    ll.display()


if __name__ == "__main__":
    main()
