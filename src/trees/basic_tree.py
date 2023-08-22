
class Node:
    def __init__(self, key, value=None, left=None, right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right

def add(root, key, value=None):
    if root == None:
        root = Node(key, value=value)
        return root
    else: 
        if key < root.key:
            if root.left == None:
                root.left = Node(key, value=value)
            else:
                add(root.left, key, value=value)
        else:
            if root.right == None:
                root.right = Node(key, value=value)
            else:
                add(root.right, key, value=value)
        return root

if __name__ == '__main__':

    root = None

    root = add(root, 10)
    root = add(root, 9)
    root = add(root, 15)
    root = add(root, 11)

    print(root.key, root.value)
    print(root.left.key, root.left.value)
    print(root.right.left.key)

