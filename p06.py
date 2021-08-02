# Find out whether a list is a palindrome

from linked_list.sll import sll


def is_palindrome(ll):
    curr = ll.head
    temp = []

    while curr != None:
        temp.append(curr.data)
        curr = curr.link

    # reset current position
    curr = ll.head
    while curr != None:
        elem = temp.pop()
        if curr.data == elem:
            curr = curr.link
        else:
            break

    if curr == None:
        return True
    else:
        return False


def main():
    values = input("Enter elements:").split()
    ll = sll()
    for elem in values:
        ll.insert(elem)

    result = is_palindrome(ll)
    print(result)


if __name__ == "__main__":
    main()
