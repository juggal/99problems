class Node:
    def __init__(self, data=None):
        self.data = data
        self.link = None


class sll:
    def __init__(self, head=None):
        self.head = head

    def insert(self, data):
        if self.head == None:
            self.head = Node(data)
        else:
            curr = self.head
            while curr.link != None:
                curr = curr.link
            curr.link = Node(data)

    def display(self):
        curr = self.head
        result = ''
        while curr != None:
            result += str(curr.data) + "->"
            curr = curr.link
        result = result.strip("->")
        print(result)

    def get_length(self):
        curr = self.head
        length = 0

        while curr != None:
            length += 1
            curr = curr.link

        return length

    def get_element(self, pos):
        curr = self.head
        count = 1

        while curr != None:
            if count == pos:
                return curr.data

            curr = curr.link
            count += 1
