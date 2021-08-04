# Insert an element at a given position into a list

from linked_list.sll import sll, Node


def insert_at(ll, pos, data):
    """
    Insert an element to specified position in given linked list

    Parameters
    __________
    ll: sll
        linked list on which to be operated on
    pos: int
        position at which to insert an element
    data: any
        data to be stored in the node

    Returns
    _______
    None
    """
    curr = ll.head
    count = 1
    prev = None

    if pos == 1:
        node = Node(data)
        node.link = curr
        ll.head = node
    elif pos > ll.get_length():
        while curr.link != None:
            curr = curr.link

        node = Node(data)
        curr.link = node
    else:
        while curr != None:
            if count == pos:
                node = Node(data)
                prev.link = node
                node.link = curr

            prev = curr
            curr = curr.link
            count += 1


def main():
    values = input("Enter elements:").split()
    data = input("Enter new element:")
    n = int(input("Enter position:"))
    ll = sll()

    for elem in values:
        ll.insert(elem)

    insert_at(ll, n, data)
    ll.display()


if __name__ == "__main__":
    main()
