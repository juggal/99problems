# Remove the K'th element from a list

from linked_list.sll import sll


def remove_at(ll, pos):
    curr = ll.head
    count = 1
    prev = None

    if pos == 1:
        ll.head = curr.link
    else:
        while curr != None:
            if count == pos:
                prev.link = curr.link

            prev = curr
            curr = curr.link
            count += 1


def main():
    values = input("Enter elements:").split()
    n = int(input("Remove element at:"))
    ll = sll()

    for elem in values:
        ll.insert(elem)

    remove_at(ll, n)
    ll.display()


if __name__ == "__main__":
    main()
