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
    item = ll.head
    ll_length = 1
    while item.next:
        ll_length += 1
        item = item.next
    length = ll_length
    get_item = length - m
    item = ll.head
    if m <= length:
        for i in range(get_item):
            item = item.next
    else:
        return "Provided position is not in the list"
    return item.data


e1 = Node(1)
e2 = Node(2)
e3 = Node(3)
e4 = Node(4)

ll = LinkedList(e1)
ll.append(e2)
ll.append(e4)
ll.append(e3)

print question5(ll, 2)
# Expected: 4

print question5(ll, 3)
# Expected: 2

print question5(ll, 6)
# Expected: Provided position is not in the list

print question5(ll, -1)
# Expected: Please supply number 1 or higher