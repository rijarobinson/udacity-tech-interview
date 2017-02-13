# STUDY BIG O SOME MORE

# """Question 3
# -Given an undirected graph G, find the minimum spanning tree within G.
# -A minimum spanning tree connects all vertices in a graph with the smallest
#   possible total weight of edges.
# -Your function should take in and return an adjacency list structured
#   like this:"""


# {'A': [('B', 2)],'B': [('A', 2), ('C', 5)],'C': [('B', 5)]}


# Clarifying the Question/Assumptions:
# We want to return a dictionary containing the list of vertices and edges
# that are a result of determining the miminum spanning tree for the
# given edge weights


    # Assumptions:
    # All edges are undirected
    # There are no parallel edges, and no vertices are self-connected
    # The returned list does not have to be sorted
    # Edges are non-negative integers
    # Vertices are letters

# Confirming input/output:
# We are taking in a graph, G, being represented by a dictionary. All edges
#   in both directions are represented in the dictionary.
# Output is a dictionary, formatted as the input, which only contains
#   vertices and edges necessary to represent the minimum spanning tree

# Test Cases:
# Some examples of test cases might be:
    # Given Udacity case:
    # {'A': [('B', 2)], 'B': [('A', 2), ('C', 5)], 'C': [('B', 5)]}
    # The mst is {'A': [('B', 2)], 'B': [('A', 2), ('C', 5)], 'C': [('B', 5)]}
    #   with a weight of 7

    # A slightly more complex example:
    #   (https://en.wikipedia.org/wiki/Minimum_spanning_tree#/media/File:Multiple_minimum_spanning_trees.svg)  #NOQA
    # H = {'A': [('B', 1), ('D', 4), ('E', 3)],
    #      'B': [('A', 1), ('D', 4), ('E', 2)],
    #      'C': [('E', 4), ('F', 5)],
    #      'D': [('A', 4), ('B', 4), ('E', 4)],
    #      'E': [('A', 3), ('B', 2), ('C', 4), ('D', 4), ('F', 7)],
    #      'F': [('C', 5), ('E', 7)]}
    # Allows for checking of more edges and possible combinations
    # The mst is {'A': [('B', 1), ('D', 4)], 'C': [('E', 4), ('F', 5)],
    #             'B': [('E', 2), ('A', 1)], 'E': [('B', 2), ('C', 4)],
    #             'D': [('A', 4)], 'F': [('C', 5)]} with a weight of 16

# Brainstorming

# To get the minimum spanning tree, I need to go through each item in the
# given vertices/edges and select the smallest possible weights of edges
# that connect all vertices. Each edge is to be traversed only once. It helps
# me to keep in mind a real-world example where you might be laying network
# lines and the cost of going from point to point.

# I decided that it would be easier to work with a 2d list rather than
# dictionary, so I wrote a function to first translate to a list. I think
# that this will make it easier to sort by edge weight.

# I review Kruskal's algorithm which helps clarify the concept in my mind.
# I draw a graph representation of the inputs and followed Kruskal's
# algorithm to come up with an answer.

# I want to start with checking the smallest edge values first. In order
# to do this, I figure I need to sort the vertex,vertex,edge lists by edge
# value, then go through the list, select the lowest value edge, and
# check to see if the vertices have already been visited.

# I will keep track of vertices/edges I have visited by eliminating them from
# the graph2D list until they have all been eliminated. Thus, I'll check
# to see if there are still items in graph2D before checking for an item, which
# will determine my iterations.

# Once I find a vertex pair and edge that match my criteria for being the
# smallest edge available that has not had both vertices visted, I will add
# it to the list of results, delete it (and its inverse) from graph2D, then
# check the next item in graph2D.

# Finally, I need a way to convert the list back to a dictionary format, so I
# will create each result in the desired format and add it to my dictionary.

# -------------------------M NEED TO DO THIS:------------------------------
# In big O notation for time, there are about 6 lines in constant time.


from operator import itemgetter

# Convert this to 2-d list with vertex, vertex, edge value
def convertToList(G):
    graph2D = []
    # For each item in G, create a list of vertex, vertex,
    # connecting edge value and append to graph2D list
    for vertex in G:
        fromVertex = vertex
        for item in G[vertex]:
            graph2D.append([vertex, item[0], item[1]])
    return graph2D

def question3(G):
    returnDict, result = {}, []
    selectedItem, smallestEdge = None, None
    # Sort graph2D by edge values smallest to largest
    graph2D = sorted(convertToList(G), key=itemgetter(2))
    # Go through the items in the graph2D list
    while len(graph2D):
        # Set the first item to check to the smallest (first) item in
        # the list
        smallestEdge,selectedItem = graph2D[0][2], graph2D[0]
        # These variables allow for checking if vertices have already
        # been visited
        checkOne, checkTwo = False, False
        # Only do this if there are items in the result list to check
        # if the item is already in the list, otherwise continue
        if len(result):
            for r in result:
                # If the first vertex in the graph2D item is in result,
                # note that and check the 2nd vertex
                if selectedItem[0] in r:
                    checkOne = True
                    for r in result:
                        # If the 2nd vertex in the graph2D item is in result,
                        # return True for both checkOne & checkTwo, so that
                        # we can just remove the item from graph2D and move
                        # to the next item since they have already been visited
                        if selectedItem[1] in r:
                            checkTwo = True
        if checkOne is True and checkTwo is True:
            if selectedItem in graph2D:
                graph2D.remove(selectedItem)
                c,d,e = selectedItem
                # We also need to remove the inverse combination of
                # the two vertices
                if [d,c,e] in graph2D:
                    graph2D.remove([d,c,e])
        else:
            # If only one or neither vertex is found, we can then add the
            # selected vertices and edge (and its inverse) to the result list
            result.append(selectedItem)
            if selectedItem in graph2D:
                graph2D.remove(selectedItem)
            u,v,w = selectedItem
            reverseOfSelected = v,u,w
            result.append(reverseOfSelected)
            if [v,u,w] in graph2D:
                graph2D.remove([v,u,w])
    # To create the return in the correct format, we go through the result list
    # and format to a dictionary
    for edges in sorted(result):
        key, listValues = edges[0], (edges[1], edges[2])
        # If the primary vertex has already been added to the dictionary,
        # add the new 2nd vertex and edge values to the existing key, otherwise
        # create a new key and add it there
        if key in returnDict:
            returnDict[key].append(listValues)
        else:
            returnDict.update({key: [listValues]})
    # Assuming dictionary list does not have to be sorted
    return returnDict


# Test cases

G = {'A': [('B', 2)],'B': [('A', 2), ('C', 5)],'C': [('B', 5)]}

H = {'A': [('B', 1), ('D', 4), ('E', 3)], 'B': [('A', 1), ('D', 4), ('E', 2)], 'C': [('E', 4), ('F', 5)],
           'D': [('A', 4), ('B', 4), ('E', 4)], 'E': [('A', 3), ('B', 2), ('C', 4), ('D', 4), ('F', 7)],
           'F': [('C', 5), ('E', 7)]}

# Udacity test case should be {'A': [('B', 2)], 'C': [('B', 5)]}
print question3(G)
# Marija test case should be {'A': [('B', 1), ('D', 4)], 'C': [('E', 4), ('F', 5)], 'B': [('E', 2)]}
print question3(H)