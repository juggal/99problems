class Node:
    def __init__(self, data=None):
        self.data = data
        self.link = None


class sll:
    def __init__(self):
        self.head = None

    def insert(self, data):
        if self.head == None:
            self.head = Node(data)
        else:
            curr = self.head
            while curr.link != None:
                curr = curr.link
            curr.link = Node(data)

    def display(self, sublist=False):
        curr = self.head
        result = ''
        while curr != None:
            result += str(curr.data) + "->"
            curr = curr.link
        result = result.strip("->")
        print(result)
