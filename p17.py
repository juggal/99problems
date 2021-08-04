# Split a list into two parts; the length of the first part is given

from linked_list.sll import sll, Node


def list_split(ll, pos):
    """
    Split given linked list into two parts from given position

    Parameters
    __________
    ll: sll
        linked list on which to be operated on
    pos: int
        position from where to split the linked list

    Returns
    _______
    sll
        Splitted half of the linked list
    """
    curr = ll.head
    count = 1
    temp_list = None

    while curr != None:
        if count == pos:
            temp_list = sll(curr.link)
            curr.link = None
            break
        curr = curr.link
        count += 1

    return temp_list


def main():
    values = input("Enter elements:").split()
    n = int(input("Split at:"))
    ll = sll()

    for elem in values:
        ll.insert(elem)

    temp = list_split(ll, n)
    ll.display()
    temp.display()


if __name__ == "__main__":
    main()
