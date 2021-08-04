class Node:
    """A class used to represent Node in linked list"""

    def __init__(self, data=None, link=None):
        """
        Parameters
        ----------
        data: any, optional
            actual data to be stored in Node
        link: Node, optional
            reference to another Node object

        Returns
        -------
        None
        """
        self.data = data
        self.link = link


class sll:
    """Class used to reperesent linked list data structure"""

    def __init__(self, head=None):
        """
        Parameters
        ----------
        head: Node, optional
            Store reference to initial Node of linked list

        Returns
        -------
        None
        """
        self.head = head

    def insert(self, data):
        """
        Insert a new Node at the end of linked list

        Parameters
        ----------
        data: any
            data to be added to linked list

        Returns
        -------
        None
        """
        if self.head == None:
            self.head = Node(data)
        else:
            curr = self.head
            while curr.link != None:
                curr = curr.link
            curr.link = Node(data)

    def display(self, end="->"):
        """
        Display all linked list elements

        Parameters
        ----------
        end: str, optional
            Seprator to be added between elements when displayed

        Returns
        -------
        None
        """
        curr = self.head
        result = ''
        while curr != None:
            result += str(curr.data) + end
            curr = curr.link
        result = result.strip(end)
        print(result)

    def get_length(self):
        """
        Get the length of the linked list

        Parameters
        ----------
        None

        Returns
        -------
        int
            legnth of linked list

        """
        curr = self.head
        length = 0

        while curr != None:
            length += 1
            curr = curr.link

        return length

    def get_element(self, pos):
        """
        Get the element at specified position or returns None if position does not exist

        Parameters
        ----------
        pos: int
            Position in linked list to fetch the element from

        Returns
        -------
        any
            Element found at specified position
        """
        curr = self.head
        count = 1

        while curr != None:
            if count == pos:
                return curr.data

            curr = curr.link
            count += 1
        return None
