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


# Assumptions:
# Do not need to make a BST first
# Will return None if no common ancestor found
# Both nodes provided are in the tree

# Test Cases:
#   Udacity's case
#   print question4([[0, 1, 0, 0, 0],
#                    [0, 0, 0, 0, 0], [0, 0, 0, 0, 0],
#                    [1, 0, 0, 0, 1], [0, 0, 0, 0, 0]],
#                     3,
#                     1,
#                     4)
#   Should return the root, 3

#   print question4([[0, 1, 1, 0, 0, 0],
#                    [0, 0, 0, 0, 0, 0],
#                    [0, 0, 0, 0, 1, 1],
#                    [1, 0, 0, 0, 0, 0],
#                    [0, 0, 0, 0, 0, 0],
#                    [0, 0, 0, 0, 0, 0]],
#                     3,
#                     4,
#                     5)
#   I included this case because it has two common ancestors, and I wanted to
#   make sure my algorithm returns the *least* common ancestor
#   This should return 2

#   print question4([[0, 1, 1, 0, 0, 0],
#                    [0, 0, 0, 0, 0, 0],
#                    [0, 0, 0, 0, 1, 1],
#                    [1, 0, 0, 0, 0, 0],
#                    [0, 0, 0, 0, 0, 0],
#                    [0, 0, 0, 0, 0, 0]],
#                     3,
#                     1,
#                     5)
#   Testing with the same tree, but one of the ancestors being up a level
#   Should return 0

def question4(T, r, n1, n2):
    # Create a list of dictionaries to hold all relationships
    # and a list for each of the n1 and n2 ancestors for comparison
    pc_rel, n1_ancestors, n2_ancestors = [], [], []
    # Create variables to hold the next item in the tree for comparison
    n1_next, n2_next = None, None
    # Go through each item in the maxtrix and determine parent-child
    # relationships and append each pair to pC_Rel list
    for t in T:
        # Go through the inner list and check if the node contains a child node
        # if so, append to the parent/child list
        for m in range(len(t)):
            if t[m] == 1:
                pc_rel.append({'parent': T.index(t), 'child': m})
    # Look at the parent/child list and create a list of parents
    # for each child that was given as n1 or n2
    for p in pc_rel:
        if p['child'] == n1:
            n1_ancestors.append(p['parent'])
            n1_next = p['parent']
            for p in pc_rel:
                if p['child'] == n1_next:
                    n1_ancestors.append(p['parent'])
        if p['child'] == n2:
            n2_ancestors.append(p['parent'])
            n2_next = p['parent']
            for p in pc_rel:
                if p['child'] == n2_next:
                    n2_ancestors.append(p['parent'])
    # Now we will compare the lists and find the common ancestors, then
    # return the lowest in the tree (that closest to the beginning of the list)
    any_in = [x for x in n1_ancestors if x in n2_ancestors]
    if any_in:
        return any_in[0]

print question4([[0, 1, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0],
                 [1, 0, 0, 0, 1], [0, 0, 0, 0, 0]], 3, 1, 4)
print question4([[0, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 1],
                 [1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0]], 3, 4, 5)
print question4([[0, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 1],
                 [1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0]], 3, 1, 5)
