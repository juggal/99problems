# Extract a slice from a list

from linked_list.sll import sll


def list_slice(ll, start, end):
    curr = ll.head
    count = 1
    start_link = None
    end_link = None
    temp_list = sll()

    while curr != None:
        if count == start:
            start_link = curr
        if count == end:
            end_link = curr
        curr = curr.link
        count += 1

    curr = start_link
    while curr != end_link.link:
        temp_list.insert(curr.data)
        curr = curr.link

    return temp_list


def main():
    values = input("Enter elements:").split()
    pos = input("Enter start & end:").split()
    ll = sll()

    for elem in values:
        ll.insert(elem)

    temp = list_slice(ll, int(pos[0]), int(pos[1]))
    temp.display()


if __name__ == "__main__":
    main()
