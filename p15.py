# Replicate the elements of a list a given number of times

from linked_list.sll import sll, Node


def repli(ll, repeat):
    curr = ll.head

    while curr != None:
        temp_link = curr.link
        i = 1
        while i < repeat:
            node = Node(curr.data)
            curr.link = node
            curr = curr.link
            i += 1

        curr.link = temp_link
        curr = curr.link


def main():
    values = input("Enter elements:").split()
    repeat = int(input("Enter no of time to repeat elements:"))
    ll = sll()

    for elem in values:
        ll.insert(elem)

    repli(ll, repeat)
    ll.display()


if __name__ == "__main__":
    main()
