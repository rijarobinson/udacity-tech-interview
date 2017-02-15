# Question 3
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
    # There are no parallel edges
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

    # Case with a self-connected vertex
    # I = {'A': [('B', 2), ('A', 1)],'B': [('A', 2), ('C', 5)],'C': [('B', 5)]}
    # The mst is {'A': [('B', 2)], 'C': [('B', 5)], 'B': [('A', 2), ('C', 5)]}
    # with a weight of 7



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
# the graph_2d list until they have all been eliminated. Thus, I'll check
# to see if there are still items in graph_2d before checking for an item, which
# will determine my iterations.

# Once I find a vertex pair and edge that match my criteria for being the
# smallest edge available that has not had both vertices visted, I will add
# it to the list of results, delete it (and its inverse) from graph_2d, then
# check the next item in graph_2d.

# Finally, I need a way to convert the list back to a dictionary format, so I
# will create each result in the desired format and add it to my dictionary.

# -------------------------M NEED TO DO THIS:------------------------------
# In big O notation for time, there are about 6 lines in constant time.


from operator import itemgetter

# Convert this to 2-d list with vertex, vertex, edge value
def convertToList(G):
    graph_2d = []
    # For each item in G, create a list of vertex, vertex,
    # connecting edge value and append to graph_2d list
    for vertex in G:
        from_vertex = vertex
        for item in G[vertex]:
            graph_2d.append([vertex, item[0], item[1]])
    return graph_2d

def question3(G):
    return_dict, result = {}, []
    selected_item, smallest_edge = None, None
    # Sort graph_2d by edge values smallest to largest
    graph_2d = sorted(convertToList(G), key=itemgetter(2))
    # Go through the items in the graph_2d list
    while len(graph_2d):
        # Set the first item to check to the smallest (first) item in
        # the list
        smallest_edge,selected_item = graph_2d[0][2], graph_2d[0]
        # These variables allow for checking if vertices have already
        # been visited
        check_one, check_two = False, False
        # Only do this if there are items in the result list to check
        # if the item is already in the list, otherwise continue
        if len(result):
            for r in result:
                # If the first vertex in the graph_2d item is in result,
                # note that and check the 2nd vertex
                if selected_item[0] in r:
                    check_one = True
                    for r in result:
                        # If the 2nd vertex in the graph_2d item is in result,
                        # return True for both check_one & check_two, so that
                        # we can just remove the item from graph_2d and move
                        # to the next item since they have already been visited
                        if selected_item[1] in r:
                            check_two = True
        if (check_one is True and check_two is True or
            selected_item[0] == selected_item[1]):
            if selected_item in graph_2d:
                graph_2d.remove(selected_item)
                c,d,e = selected_item
                # We also need to remove the inverse combination of
                # the two vertices
                if [d,c,e] in graph_2d:
                    graph_2d.remove([d,c,e])
        else:
            # If only one or neither vertex is found, we can then add the
            # selected vertices and edge (and its inverse) to the result list
            result.append(selected_item)
            if selected_item in graph_2d:
                graph_2d.remove(selected_item)
            u,v,w = selected_item
            reverse_selected = v,u,w
            result.append(reverse_selected)
            if [v,u,w] in graph_2d:
                graph_2d.remove([v,u,w])
    # To create the return in the correct format, we go through the result list
    # and format to a dictionary
    for edges in sorted(result):
        key, list_values = edges[0], (edges[1], edges[2])
        # If the primary vertex has already been added to the dictionary,
        # add the new 2nd vertex and edge values to the existing key, otherwise
        # create a new key and add it there
        if key in return_dict:
            return_dict[key].append(list_values)
        else:
            return_dict.update({key: [list_values]})
    # Assuming dictionary list does not have to be sorted
    return return_dict


# Test cases

G = {'A': [('B', 2)],'B': [('A', 2), ('C', 5)],'C': [('B', 5)]}

H = {'A': [('B', 1), ('D', 4), ('E', 3)], 'B': [('A', 1), ('D', 4), ('E', 2)], 'C': [('E', 4), ('F', 5)],
           'D': [('A', 4), ('B', 4), ('E', 4)], 'E': [('A', 3), ('B', 2), ('C', 4), ('D', 4), ('F', 7)],
           'F': [('C', 5), ('E', 7)]}

I = {'A': [('B', 2), ('A', 1)],'B': [('A', 2), ('C', 5)],'C': [('B', 5)]}


# Udacity test case should be {'A': [('B', 2)], 'C': [('B', 5)], 'B': [('A', 2), ('C', 5)]}
print question3(G)
# Marija test case should be {'A': [('B', 1), ('D', 4)], 'C': [('E', 4), ('F', 5)], 'B': [('E', 2)]}
print question3(H)

# Edge case checks to see if vertices is self-connected
# Expected: {'A': [('B', 2)], 'C': [('B', 5)], 'B': [('A', 2), ('C', 5)]}
print question3(I)