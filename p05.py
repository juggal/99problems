# Reverse a list

from linked_list.sll import sll


def reverse_list(ll):
    curr = ll.head
    temp = None
    prev = None

    while curr != None:
        temp = curr.link
        curr.link = prev
        prev = curr
        curr = temp

    ll.head = prev


def main():
    values = input("Enter elements:").split()
    ll = sll()
    for elem in values:
        ll.insert(elem)

    print("Before")
    ll.display()

    reverse_list(ll)
    print("After")
    ll.display()


if __name__ == "__main__":
    main()
