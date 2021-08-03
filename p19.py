# Rotate a list N places to the left

from linked_list.sll import sll


def list_split(ll, pos):
    curr = ll.head
    count = 1
    temp_list = None

    if pos < 0:
        pos = ll.get_length() + pos

    while curr != None:
        if count == pos:
            temp_list = sll(curr.link)
            curr.link = None
            break
        curr = curr.link
        count += 1

    return temp_list


def list_rotate(ll, n):
    curr = ll.head
    count = 1

    split_2 = list_split(ll, n)

    while curr != None:
        split_2.insert(curr.data)
        curr = curr.link

    return split_2


def main():
    values = input("Enter elements:").split()
    n = int(input("Rotate:"))
    ll = sll()

    for elem in values:
        ll.insert(elem)

    rotated_list = list_rotate(ll, n)
    rotated_list.display()


if __name__ == "__main__":
    main()
