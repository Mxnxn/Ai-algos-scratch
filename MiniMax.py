import numpy as np


class Node():
    """A node class for A* Pathfinding"""

    def __init__(self, parent=None, position=None, score=None,children = None,hasChildren = False):
        self.parent = parent
        self.position = position
        self.score = score
        self.children = children
        self.hasChildren = hasChildren

    def is_leaf(self):
        return False if self.children else True

    def __eq__(self, parent):
        return self.parent == parent

    def __repr__(self):
        return 'parent: {}, position:{}, score: {}, children: {}\n'.format(self.parent, self.position, self.score, self.children)


class Minimax():
    def __init__(self):
        self.tree = []
        self.maxDepth = 4
        # self.depth = 2
        # self.values = [0, 0, 0, 7, 69, 70, 34]
        # self.nodes = 7

        self.depth = 6
        self.values = [0, 0, 0, 0, 0, 0, 0,  28, 19, 90, 91, 46, 75, 76, 80]
        self.nodes = 15
        self.iter = 0
        self.answer = 0
        self.generateTree()
        self.answer = self.minimax(0, self.depth, True)

    def generateTree(self):
        """Returns a list of tuples as a path from the given start to the given end in the given maze"""
        parent = 0
        counter = 0
        for i in range(0,self.nodes):
            if i % 2 != 0 and i > 1:
                parent+=1
            if i > self.depth:
                self.tree.append(Node(parent,i,self.values[i],None))
            else:
                self.tree.append(Node(parent,i,self.values[i],[counter+1,counter+2]))
            counter += 2

    def addNodes(self, parentNode, counter):
        leftChild = self.addLeftChild(parentNode.position, counter, self.values[parentNode.position])
        rightChild = self.addRightChild(parentNode.position, counter, self.values[parentNode.position])
        parentNode.children = [leftChild,rightChild]
        return parentNode
    
    def addLeftChild(self,position, score):
        return Node(position,position+1,score,[])

    def addRightChild(self,position, score):
        return Node(position,position+3,score,[])

    def minimax(self, position, depth, isMaximiser):
        self.iter += 1
        if depth == 0 or self.tree[position].is_leaf():
            return self.tree[position].score

        if isMaximiser:
            maxEvaluation = -float('inf')
            for child in self.tree[position].children:
                for nodes in self.tree:
                    if child == nodes.position:
                        eval = self.minimax(child, depth - 1, False)
                        maxEvaluation = max(eval,maxEvaluation)
            return maxEvaluation

        else:
            minEvaluation = float('inf')
            for child in self.tree[position].children:
                for nodes in self.tree:
                    if child == nodes.position:
                        eval = self.minimax(child, depth - 1, True)
                        minEvaluation = min(minEvaluation, eval)
            return minEvaluation

if __name__ == '__main__':
    Obj = Minimax()
    print('Answer: ',Obj.answer)
    print("Total Iter:", Obj.iter)

