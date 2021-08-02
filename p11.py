# Modified run-length encoding.

from linked_list.sll import sll


def encode(ll):
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
