# This is the complete working code
# Work in progress, It works, but always trying to improve

# """Question 3
# -Given an undirected graph G, find the minimum spanning tree within G.
# -A minimum spanning tree connects all vertices in a graph with the smallest possible total weight of edges.
# -Your function should take in and return an adjacency list structured like this:"""


# {'A': [('B', 2)],'B': [('A', 2), ('C', 5)],'C': [('B', 5)]}

from operator import itemgetter

# convert this to 2-d list with vertex, vertex, edge value

def convertToList(G):
    graph2D = []
    for vertex in G:
        fromVertex = vertex
        for item in G[vertex]:
            graph2D.append([vertex, item[0], item[1]])
    return graph2D

def question3(G):
    returnDict, result = {}, []
    selectedItem, smallestEdge = None, None
    graph2D = sorted(convertToList(G), key=itemgetter(2))
    mst = 0
    while len(graph2D):
        smallestEdge,selectedItem = graph2D[0][2], graph2D[0]
        checkOne, checkTwo = False, False
        if len(result):
            for r in result:
                if selectedItem[0] in r:
                    checkOne = True
                    for r in result:
                        if selectedItem[1] in r:
                            checkTwo = True
        if checkOne is True and checkTwo is True:
            if selectedItem in graph2D:
                graph2D.remove(selectedItem)
                c,d,e = selectedItem
                if [d,c,e] in graph2D:
                    graph2D.remove([d,c,e])
        else:
            result.append(selectedItem)
            if selectedItem in graph2D:
                graph2D.remove(selectedItem)
            u,v,w = selectedItem
            if [v,u,w] in graph2D:
                graph2D.remove([v,u,w])
    for edges in sorted(result):
        key, listValues = edges[0], (edges[1], edges[2])
        if key in returnDict:
            returnDict[key].append(listValues)
        else:
            returnDict.update({key: [listValues]})
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