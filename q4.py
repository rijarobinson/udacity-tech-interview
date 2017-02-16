# """Question 4
# -Find the least common ancestor between two nodes on a binary search tree.
# -The least common ancestor is the farthest node from the root that is
#   an ancestor of both nodes.
# -For example, the root is a common ancestor of all nodes on the tree, but
#   if both nodes are descendents of the root's left child, then that left
#   child might be the lowest common ancestor.
# -You can assume that both nodes are in the tree, and the tree itself
#   adheres to all BST properties.

# -The function definition should look like question4(T, r, n1, n2), where T
#   is the tree represented as a matrix, where the index of the list
#   is equal to the integer stored in that node and a 1 represents a child node,
#   r is a non-negative integer representing the root, and n1 and n2 are
#   non-negative integers representing the two nodes in no
#   particular order. For example, one test case might be"""

# question4([[0, 1, 0, 0, 0],
#            [0, 0, 0, 0, 0],
#            [0, 0, 0, 0, 0],
#            [1, 0, 0, 0, 1],
#            [0, 0, 0, 0, 0]],
#           3,
#           1,
#           4)

# """and the answer would be 3.""" (least common ancestor)


# Clarifying the Question/Assumptions:
# We want to return an integer representing the node which n1 and n2
# have in common as an ancestor that is lowest on the tree, given the
# tree structure in a matrix


    # Assumptions:
    # A node is its own ancestor
    # Will return None if no common ancestor found

# Confirming input/output:
# We are taking in a (what we are assuming is a) BST being represented
#   by a matrix, the node to be designated as the root, and two nodes, n1 & n2
#   that are assumed to have a common ancestor
# Output is a number that represents to the ancestor that is common to both
#   n1 and n2 that is lowest on the tree

# Test Cases:
#   Udacity's case
#   print question4([[0, 1, 0, 0, 0],
#                    [0, 0, 0, 0, 0],
#                    [0, 0, 0, 0, 0],
#                    [1, 0, 0, 0, 1],
#                    [0, 0, 0, 0, 0]],
#                     3,
#                     1,
#                     4)
#   Should return the root, 3

# print question4([[0, 0, 0, 0, 0, 0],
#                  [1, 0, 0, 1, 0, 0],
#                  [0, 0, 0, 0, 0, 0],
#                  [0, 0, 1, 0, 0, 1],
#                  [0, 0, 0, 0, 1, 0],
#                  [0, 0, 0, 0, 0, 0]],
#                   1,
#                   4,
#                   5)
#   Should return 5

# print question4([[0, 1, 1, 0, 0, 0, 0, 0],
#                  [0, 0, 0, 0, 0, 0, 0, 0],
#                  [0, 0, 0, 0, 0, 0, 0, 0],
#                  [1, 0, 0, 0, 0, 0, 1, 0],
#                  [0, 0, 0, 0, 0, 1, 0, 0],
#                  [0, 0, 0, 0, 0, 0, 0, 0],
#                  [0, 0, 0, 0, 1, 0, 0, 1],
#                  [0, 0, 0, 0, 0, 0, 0, 0]],
#                   3,
#                   5,
#                   7)
#   Should return 6

# print question4([[0, 0, 0, 0, 0, 0],
#                  [1, 0, 0, 1, 0, 0],
#                  [0, 0, 0, 0, 0, 0],
#                  [0, 0, 1, 0, 0, 1],
#                  [0, 0, 0, 0, 1, 0],
#                  [0, 0, 0, 0, 0, 0]],
#                   1,
#                   7,
#                   5)
#   Should return Node not in matrix


# Brainstorming:
# First, I draw the BST using the matrix to visualize it and get an idea
# of what the test case must return. What I want to do is take advantage
# the BST rules so I will create a BST tree. Once I have the tree,
# I can add the nodes given, and recursively search for the lowest
# common ancestor based on the value of the nodes in relation to r,
# which will change if no common ancestor is available for that
# recursion.

# I will put in place a check first to see if the nodes qualify
# for the root to be the lca, that is, if n1 and n2 are on different
# sides of the root.

# I also want to check to make sure the given nodes are in the tree.


# First solution, see more efficient solution below
# # Helper-build the relationships
# def buildRelationships(T):
#     # Create a list of dictionaries to hold all relationships
#     pc_rel = []
#     # Go through each item in the maxtrix and determine parent-child
#     # relationships and append each pair to pC_Rel list
#     for t in T:
#         # Go through the inner list and check if the node contains a child node
#         # if so, append to the parent/child list
#         for m in range(len(t)):
#             if t[m] == 1:
#                 pc_rel.append({'parent': T.index(t), 'child': m})
#     return pc_rel


# def question4(T, r, n1, n2):
#     # list for each of the n1 and n2 ancestors for comparison
#     n1_ancestors, n2_ancestors = [], []
#     n1_next, n2_next = None, None
#     pc_rel = buildRelationships(T)
#     # Look at the parent/child list and create a list of parents
#     # for each child that was given as n1 or n2
#     for p in pc_rel:
#         if p['child'] == n1:
#             n1_ancestors.append(p['parent'])
#             n1_next = p['parent']
#             for p in pc_rel:
#                 if p['child'] == n1_next:
#                     n1_ancestors.append(p['parent'])
#         if p['child'] == n2:
#             n2_ancestors.append(p['parent'])
#             n2_next = p['parent']
#             for p in pc_rel:
#                 if p['child'] == n2_next:
#                     n2_ancestors.append(p['parent'])
#     # Now we will compare the lists and find the common ancestors, then
#     # return the lowest in the tree (that closest to the beginning of the list)
#     any_in = [x for x in n1_ancestors if x in n2_ancestors]
#     if any_in:
#         return any_in[0]

# Create a node class
class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        self.helper_insert(self.root, new_val)

    def helper_insert(self, current, new_val):
        if current.value < new_val:
            if current.right:
                self.helper_insert(current.right, new_val)
            else:
                current.right = Node(new_val)
        else:
            if current.left:
                self.helper_insert(current.left, new_val)
            else:
                current.left = Node(new_val)


    # def print_tree(self):
    #     """Print out all tree nodes
    #     as they are visited in
    #     a pre-order traversal."""
    #     traversal = []
    #     start = self.root
    #     if start != None:
    #         return "-".join(self.preorder_print(start, traversal))
    #     else:
    #         return "no root"


    # def preorder_print(self, start, traversal):
    #     """Helper method - use this to create a
    #     recursive print solution."""
    #     if start:
    #         traversal.append(str(start.value))
    #         self.preorder_print(start.left, traversal)
    #         self.preorder_print(start.right, traversal)
    #     return traversal



def createTree(tree, T):
    for t in T:
        for i in range(len(t)):
            if t[i] == 1:
                tree.insert(i)
    return tree


def checkPosition(n1, n2, r):
    # print "n1, n2, r: %s" % str(n1) + ", " + str(n2) + ", " + str(r.value)
    if (n1 <= r.value and n2 >= r.value or
        n1 >= r.value and n2 <= r.value):
        return r.value
    elif n1 < r.value and n2 < r.value:
        # print "n1 and n2 are to the left"
        r = r.left
        if r:
            # print "r is now: %s" % r.value
            return checkPosition(n1, n2, r)
    elif n1 > r.value and n2 > r.value:
        # print "n1 and n2 are to the right"
        r = r.right
        if r:
            # print "r is now: %s" % r.value
            return checkPosition(n1, n2, r)


def question4(T, r, n1, n2):
    if n1 <= len(T) and n2 <= len(T):
        tree = BST(r)
        createTree(tree, T)
        # print tree.print_tree()
        return checkPosition(n1, n2, tree.root)
    else:
        return "Node not in matrix"

# Test cases
# Should return 3
print question4([[0, 1, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0],
                 [1, 0, 0, 0, 1], [0, 0, 0, 0, 0]], 3, 1, 4)

# Should return 5
print question4([[0, 0, 0, 0, 0, 0], [1, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0],
                 [0, 0, 1, 0, 0, 1], [0, 0, 0, 0, 1, 0],
                 [0, 0, 0, 0, 0, 0]], 1, 4, 5)

# # Should return 6
print question4([[0, 1, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
                 [1, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 1, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0]], 3, 5, 7)

# # Should return Node not in matrix
print question4([[0, 0, 0, 0, 0, 0], [1, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0],
                 [0, 0, 1, 0, 0, 1], [0, 0, 0, 0, 1, 0],
                 [0, 0, 0, 0, 0, 0]], 1, 7, 5)