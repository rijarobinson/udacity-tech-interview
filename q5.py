# Question 5

# Clarifying the Question/Assumptions:
# We want to return the value of the mth item from the end in
#   the given linked list
# We need to build a linked list object first

    # Assumptions:
    # A negative number or 0 for m is not a valid input and should
    #   output an error message
    # The linked list is singly linked
    # Node values can be whatever we want them to be

# Confirming input/output:
# We are taking in a linked list that has already been built and
#   a positive integer
# We will return the value of the mth item from the end in the list

# Test Cases:
    # print question5(ll, 2)
    # Takes in the linked list created using the ll object and
    # returns the 2nd item from the end.
    # Should return 4.

    # print question5(ll, 6)
    # Takes in the linked list, tries to return the 6th item from the end.
    # Should return error message, since the ll nodes added do not have
    # at least 6 nodes.

    # print question5(ll, -1)
    # Takes in the linked list, tries to return the -1th item from the end.
    # Should return error message, since we do not wish to use negatives or 0.

# Brainstorming:
# The list type allows us to easily select the mth item from the end,
# and a linked list can be easily converted to a python list by iterating
# the objects using next and adding them to the list.

# I will be looking to whether this can be done more efficiently after I
# submit my project ;)

# Time and Space Efficiency:
# Since we are adding the head element then iterating through the
#   remaining items with 2 actions, worst case of question5
#   is about O(2(n - 1)) or O(n-1)?

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
    # We are handling cases where a negative number or 0
    # has been supplied
    if m <= 0:
        return "Please supply number 1 or higher"
    try:
        # If the linked list has been provided, create a list to hold the
        # values for easy selection of mth element. Append the head
        # to the list then move to the next item
        item = ll.head
        linked_list = []
        linked_list.append(item.data)
        item = item.next
        # While there are items in the linked list, continue to build the list
        # in the order of the linked list with the rest of the items.
        while item:
            linked_list.append(item.data)
            item = item.next
        # Now try to return the mth item from the end of the list. If there
        # is nothing there, return the error message
        return linked_list[-m]
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
print question5(ll, 6)
print question5(ll, -1)
