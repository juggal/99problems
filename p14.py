# Duplicate the elements of a list

from linked_list.sll import sll, Node


def dupli(ll):
    curr = ll.head

    while curr != None:
        temp_node = Node(curr.data)
        temp_link = curr.link
        curr.link = temp_node
        temp_node.link = temp_link
        curr = temp_node.link


def main():
    values = input("Enter elements:").split()
    ll = sll()

    for elem in values:
        ll.insert(elem)

    dupli(ll)
    ll.display()


if __name__ == "__main__":
    main()
