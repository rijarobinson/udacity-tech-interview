# Solutions:

# Question 1

def question1(s, t):
    if s and t:
        t, s = t.lower(), s.lower()
        if t in s:
            return False
        found = []
        for c in t:
            if c in s:
                found.append(s.index(c))
                s = s.replace((c), "/", 1)
            else:
                return False
        return check_consecutive(found)
    else:
        return "did you supply the two words?"


def check_consecutive(found):
    for i in found:
        return ((((i == max(found) and i - 1 in found) or
                (i == min(found) and i + 1 in found))) or
                (i - 1 in found and i + 1 in found))


print question1('udacity', 'AD')
# Expected: True

print question1('robin', 'robins')
# Expected: False

print question1('taco cat', 'cat taco')
# Expected: True

print question1('', '')
# Expected: did you supply the two words?

print question1('udacity', 'city')
# Expected: False

print question1('udaCity', 'tyci')
# Expected: True

print question1('marija', 'Raj')
# Expected: False

print question1('marija', 'mam')
# Expected: False


# Question 2

def question2(a):
    if "/" in a:
        return "'/' character not allowed"
    palin_build, found_palins = "", []
    p = a[::-1]
    sps = 0
    while (a != (len(a) * '/')):
        if p[sps:sps+2] in a:
            palin_build = p[sps:sps+2]
            try:
                while (palin_build + p[sps+2]) in a:
                    palin_build += p[sps+2]
                    sps += 1
                if (palin_build == palin_build[::-1] and
                        palin_build not in found_palins):
                    found_palins.append(palin_build)
                a = a.replace(palin_build, '/', 1)
            except IndexError:
                if (palin_build == palin_build[::-1] and len(palin_build) > 1 and
                        palin_build not in found_palins):
                    found_palins.append(palin_build)
                a = a.replace(palin_build, '/', 1)
                sps += 1
        else:
            a = a[::-1]
            a = a.replace(p[sps], '/', 1)
            a = a[::-1]
        sps += 1
    try:
        return (max(found_palins, key=len))
    except ValueError:
        return "No palindromes found :("

print question2('tippit')
# Expected: tippit

print question2('tip pit')
# Expected: tip pit

print question2('xymmbc')
# Expected: mm

print question2('zyjxjyzdmomomz')
# Expected: zyjxjyz

print question2('xmoxmjomz')
# Expected: No palindromes found :(


# Question 3

from operator import itemgetter

# Helper-convert this to 2-d list with vertex, vertex, edge value
def convertToList(G):
    graph_2d = []
    for vertex in G:
        from_vertex = vertex
        for item in G[vertex]:
            graph_2d.append([vertex, item[0], item[1]])
    return graph_2d


def question3(G):
    return_dict, result = {}, []
    selected_item, smallest_edge = None, None
    graph_2d = sorted(convertToList(G), key=itemgetter(2))
    while len(graph_2d):
        smallest_edge,selected_item = graph_2d[0][2], graph_2d[0]
        check_one, check_two = False, False
        if len(result):
            for r in result:
                if selected_item[0] in r:
                    check_one = True
                    for r in result:
                        if selected_item[1] in r:
                            check_two = True
        if (check_one is True and check_two is True or
            selected_item[0] == selected_item[1]):
            if selected_item in graph_2d:
                graph_2d.remove(selected_item)
                c,d,e = selected_item
                if [d,c,e] in graph_2d:
                    graph_2d.remove([d,c,e])
        else:
            result.append(selected_item)
            if selected_item in graph_2d:
                graph_2d.remove(selected_item)
            u,v,w = selected_item
            reverse_selected = v,u,w
            result.append(reverse_selected)
            if [v,u,w] in graph_2d:
                graph_2d.remove([v,u,w])
    for edges in sorted(result):
        key, list_values = edges[0], (edges[1], edges[2])
        if key in return_dict:
            return_dict[key].append(list_values)
        else:
            return_dict.update({key: [list_values]})
    return return_dict


# Test cases

G = {'A': [('B', 2)],'B': [('A', 2), ('C', 5)],'C': [('B', 5)]}
print question3(G)
# Expected: {'A': [('B', 2)], 'C': [('B', 5)], 'B': [('A', 2), ('C', 5)]}

G = {'A': [('B', 1), ('D', 4), ('E', 3)], 'B': [('A', 1), ('D', 4), ('E', 2)],
     'C': [('E', 4), ('F', 5)], 'D': [('A', 4), ('B', 4), ('E', 4)],
     'E': [('A', 3), ('B', 2), ('C', 4), ('D', 4), ('F', 7)],
     'F': [('C', 5), ('E', 7)]}
print question3(G)
# Expected: {'A': [('B', 1), ('D', 4)],
#            'C': [('E', 4), ('F', 5)], 'B': [('E', 2)]}

G = {'A': [('B', 2), ('A', 1)],'B': [('A', 2), ('C', 5)],'C': [('B', 5)]}
print question3(G)
# Expected: {'A': [('B', 2)], 'C': [('B', 5)], 'B': [('A', 2), ('C', 5)]}


# Question 4

# Helper-build the relationships
def buildRelationships(T):
    pc_rel = []
    for t in T:
        for m in range(len(t)):
            if t[m] == 1:
                pc_rel.append({'parent': T.index(t), 'child': m})
    return pc_rel


def question4(T, r, n1, n2):
    n1_ancestors, n2_ancestors = [], []
    n1_next, n2_next = None, None
    pc_rel = buildRelationships(T)
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
    any_in = [x for x in n1_ancestors if x in n2_ancestors]
    if any_in:
        return any_in[0]


# Test cases

print question4([[0, 1, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0],
                 [1, 0, 0, 0, 1], [0, 0, 0, 0, 0]], 3, 1, 4)
# Expected: 3

print question4([[0, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 1],
                 [1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0]], 3, 4, 5)
# Expected: 2

print question4([[0, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 1],
                 [1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0]], 3, 1, 5)
# Expected: 0

print question4([[0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 1],
                 [1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0]], 3, 1, 5)
# Expected: None


# Question 5

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
        linked_list = []
        linked_list.append(item.data)
        item = item.next
        while item:
            linked_list.append(item.data)
            item = item.next
        return linked_list[-m]
    except IndexError:
        return "Provided position is not in the list"

# The head of a list is it's first node.

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)

ll = LinkedList(n1)
ll.append(n2)
ll.append(n4)
ll.append(n3)

print question5(ll, 2)
# Expected: 4

print question5(ll, 6)
# Expected: Provided position is not in the list

print question5(ll, -1)
# Expected: Please supply number 1 or higher