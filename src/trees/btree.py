def b_search(key, D):
    lo = -1
    hi = len(D)
    mid = None

    while (hi - lo > 1):
        mid = (hi + lo) // 2
        if D[mid] < key:
            lo = mid
        else:
            hi = mid

    return hi

class Node:
    def __init__(self):
        self.keys = []
        self.values = []

        # children[0] = keys[0] left child
        # children[1] = keys[0] rigth child
        # children[1] = keys[1] left child

        self.children = []

        self.parent = None

    def __str__(self):
        global order
        return str(order) + ',' + str(self.keys)

class Tree:
    def __init__(self, order):
        self.order = order
        self.root = None

    def search(self, key, node=None):
        if node == None:
            node = self.root

        insert_pos = b_search(key, node.keys) 

        if len(node.children) == 0: #leaf node
            return insert_pos, node
        else:
            return self.search(key, node=node.children[insert_pos])

    def insert(self, key, value=None):
        if self.root == None:
            self.root = Node() 
            self.root.keys.append(key)
            self.root.values.append(value)
        else:
            insert_pos, node = self.search(key)
            if insert_pos == len(node.keys):
                node.keys.append(key)
                node.values.append(value)
            elif node.keys[insert_pos] == key:
                return
            else:
                #make room for the new key and value
                node.keys = node.keys[:insert_pos] \
                            + [None] \
                            + node.keys[insert_pos:] 
                node.values = node.values[:insert_pos] \
                              + [None] \
                              + node.values[insert_pos:] 
                node.keys[insert_pos] = key
                node.values[insert_pos] = value

        if len(node) > self.order:
            self.repair(node)

    def repair(self, node):
        if len(node) <= self.order:
            return
