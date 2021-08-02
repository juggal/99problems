# Find the last box of a list
from linked_list.sll import sll


def last_value(ll):
    curr = ll.head
    while curr.link != None:
        curr = curr.link
    print(curr.data)


def main():
    values = input("Enter elemenets:").split()
    ll = sll()

    for elem in values:
        ll.insert(elem)

    last_value(ll)


if __name__ == "__main__":
    main()
