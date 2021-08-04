# Drop every N'th element from a list

from linked_list.sll import sll, Node


def drop(ll, n):
    """
    Drop every N'th element from given linked list

    Parameters
    ----------
    ll: sll
        linked list on which to be operated on
    n: int
        multiples of which are used as index to drop elements

    Returns
    -------
    None
    """
    curr = ll.head
    count = 1
    prev = None

    while curr != None:
        if count % n == 0:
            prev.link = curr.link
            curr = prev.link
        else:
            prev = curr
            curr = curr.link
        count += 1


def main():
    values = input("Enter elements:").split()
    n = int(input("Nth element:"))
    ll = sll()

    for elem in values:
        ll.insert(elem)

    drop(ll, n)
    ll.display()


if __name__ == "__main__":
    main()
