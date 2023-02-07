values = [0, 0, 0, 7, 69, 70, 34, 76]

class Node:
    def __init__(self, value, position, children=None):
        self.value = value
        self.position = position
        self.children = children

    def is_leaf(self):
        return True if self.children == None else False

    def __repr__(self):
        return '\nvalue: {}, children: {}\n'.format(self.value,self.children)

def generate_tree(counter, depth):
    counter+=1
    if depth == 0:
        return Node(counter)
    else:
        children = [generate_tree(counter+1, depth - 1), generate_tree(counter+8,depth - 1)]
        return Node(counter, children)

root = generate_tree(0, 2)
print([root])