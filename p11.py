# Modified run-length encoding.

from linked_list.sll import sll


def encode(ll):
    """
    Apply run length encoding on given linked list
    if an element has no duplicate simply copied into result

    Parameters
    ----------
    ll: sll
        linked list on which to be operated on

    Returns
    -------
    str
        view of run length encoded linked list
    """
    curr = ll.head
    prev = curr.data
    result = "("
    count = 0

    while curr != None:
        if prev == curr.data:
            count += 1
        else:
            if count == 1:
                result += " " + str(prev) + " "
            else:
                result += "(" + str(count) + " " + str(prev) + ")"
            prev = curr.data
            count = 1
        curr = curr.link

    if count == 1:
        result += " " + str(prev) + ")"
    else:
        result += "(" + str(count) + " " + str(prev) + "))"

    return result


def main():
    values = input("Enter elements:").split()
    ll = sll()
    for elem in values:
        ll.insert(elem)

    print(encode(ll))


if __name__ == "__main__":
    main()
