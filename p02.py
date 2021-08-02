# Find the last but one box of a list
from linked_list.sll import sll


def last_but_one(ll):
    curr = ll.head
    while curr.link.link != None:
        curr = curr.link

    while curr != None:
        print(curr.data, end=" ")
        curr = curr.link


def main():
    values = input("Enter elements:").split()
    ll = sll()

    for elem in values:
        ll.insert(elem)

    last_but_one(ll)


if __name__ == "__main__":
    main()
