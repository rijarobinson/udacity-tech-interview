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
#   Expected: the root, 3

# print question4([[0, 0, 0, 0, 0, 0],
#                  [1, 0, 0, 1, 0, 0],
#                  [0, 0, 0, 0, 0, 0],
#                  [0, 0, 1, 0, 0, 1],
#                  [0, 0, 0, 0, 1, 0],
#                  [0, 0, 0, 0, 0, 0]],
#                   1,
#                   4,
#                   5)
#   Expected: 5

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
#   Expected: 6

# print question4([[0, 0, 0, 0, 0, 0],
#                  [1, 0, 0, 1, 0, 0],
#                  [0, 0, 0, 0, 0, 0],
#                  [0, 0, 1, 0, 0, 1],
#                  [0, 0, 0, 0, 1, 0],
#                  [0, 0, 0, 0, 0, 0]],
#                   1,
#                   7,
#                   5)
#   Expected: Node not in matrix


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



def getRightNode(tree, r):
    branch = tree[r]
    higher_node = (len(branch) - 1) - branch[::-1].index(1)
    return higher_node


def getLeftNode(tree, r):
    branch = tree[r]
    lower_node = branch.index(1)
    return lower_node


def question4(T, r, n1, n2):
    if n1 <= len(T) and n2 <= len(T):
        while not (n1 <= r and n2 >= r or
                n1 >= r and n2 <= r):
            if n1 < r and n2 < r:
                r = getLeftNode(T, r)
            elif n1 > r and n2 > r:
                r = getRightNode(T, r)
        if r:
            return r
    else:
        return "Node not in matrix"


# Test cases
print question4([[0, 1, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0],
                 [1, 0, 0, 0, 1], [0, 0, 0, 0, 0]], 3, 1, 4)
# Expected: 3

print question4([[0, 0, 0, 0, 0, 0], [1, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0],
                 [0, 0, 1, 0, 0, 1], [0, 0, 0, 0, 1, 0],
                 [0, 0, 0, 0, 0, 0]], 1, 4, 5)
# Expected: 5

print question4([[0, 1, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
                 [1, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 1, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0]], 3, 5, 7)
# Expected: 6

print question4([[0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 1, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 1, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0]], 3, 1, 2)
# Expected: 1, checks the left side

print question4([[0, 0, 0, 0, 0, 0], [1, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0],
                 [0, 0, 1, 0, 0, 1], [0, 0, 0, 0, 1, 0],
                 [0, 0, 0, 0, 0, 0]], 1, 7, 5)
# Expected: Node not in matrix
