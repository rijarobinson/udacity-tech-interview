STUDY BIG O SOME MORE

# """Question 4
# -Find the least common ancestor between two nodes on a binary search tree.
# -The least common ancestor is the farthest node from the root that is an ancestor of both nodes.
# -For example, the root is a common ancestor of all nodes on the tree, but if both nodes are descendents
#  of the root's left child, then that left child might be the lowest common ancestor.
# -You can assume that both nodes are in the tree, and the tree itself adheres to all BST properties.

# -The function definition should look like question4(T, r, n1, n2), where T is the tree represented as
# a matrix, where the index of the list
# is equal to the integer stored in that node and a 1 represents a child node, r is a non-negative integer
# representing the root, and n1 and n2 are non-negative integers representing the two nodes in no
# particular order. For example, one test case might be"""

# question4([[0, 1, 0, 0, 0],
#            [0, 0, 0, 0, 0],
#            [0, 0, 0, 0, 0],
#            [1, 0, 0, 0, 1],
#            [0, 0, 0, 0, 0]],
#           3,
#           1,
#           4)

# """and the answer would be 3.""" (least common ancestor)

# So, the answer should be common ancestor to 1, 4. Zero is not a common ancestor because it's only
# an ancestor to 0

# This is the complete working code
# Work in progress, It works, but always trying to improve

# Assumptions:
# Do not need to make a BST first

def question4(T, r, n1, n2):
    ptRel, n1Ancestors, n2Ancestors = [], [], []
    n1Next, n2Next = None, None
    for t in T:
        for m in range(len(t)):
            if t[m] == 1:
                ptRel.append({'parent': T.index(t), 'child': m})
    for p in ptRel:
        if p['child'] == n1:
            n1Ancestors.append(p['parent'])
            n1Next = p['parent']
            for p in ptRel:
                if p['child'] == n1Next:
                    n1Ancestors.append(p['parent'])
        if p['child'] == n2:
            n2Ancestors.append(p['parent'])
            n2Next = p['parent']
            for p in ptRel:
                if p['child'] == n2Next:
                    n2Ancestors.append(p['parent'])
    x, y = 0, 0
    try:
        while n1Ancestors[x] != n2Ancestors[y]:
            y += 1
            try:
                while n1Ancestors[x] != n2Ancestors[y]:
                        x += 1
            except IndexError:
                print "out of items"
            else:
                return n1Ancestors[x]
    except IndexError:
        print "out of items"
    else:
        return n1Ancestors[x]


print question4([[0, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 1],
                 [1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0]], 3, 4, 5)
print question4([[0, 1, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0],
                 [1, 0, 0, 0, 1], [0, 0, 0, 0, 0]], 3, 1, 4)
