# This is the complete working code
# Work in progress, It works, but always trying to improve

# """Question 5
# -Find the element in a singly linked list that's m elements from the end.
# -For example, if a linked list has 5 elements, the 3rd element from the end is the 3rd element.
# -The function definition should look like question5(ll, m), where ll is the first node of a linked list
#   and m is the "mth number from the end".
# -You should copy/paste the Node class below to use as a representation of a node in the linked list.
# -Return the value of the node at that position."""


# Allows us to build a linked list, from
# FSND Linked List Practice Quiz
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element


def question5(ll, m):
    if m <= 0:
        return "Please supply number 1 or higher"
    try:
        item = ll.head
        theList = []
        theList.append(item.data)
        item = item.next
        while item:
            theList.append(item.data)
            item = item.next
        return theList[-m]
    except IndexError:
        return "Provided position is not in the list"

# The head of a list is it's first node.

e1 = Node(1)
e2 = Node(2)
e3 = Node(3)
e4 = Node(4)

ll = LinkedList(e1)
ll.append(e2)
ll.append(e4)
ll.append(e3)

print question5(ll, 2)
