
from igraph import *
import random

class Tree:
    def __init__(self, vertices, bFactor):
        self.vertices = vertices
        self.bFactor = bFactor

        self. labels = []
        for i in range(100):
            val = random.randint(0, 1000)
            self.labels.append(val)

        self.graph = Graph.Tree(vertices, bFactor)

        self.graph.vs["label"] = self.labels


    def getLeaves(self):
        leaves = self.graph.vs.select(_degree=1)["label"] 
        return leaves

    def deleteLeaves(self):
        leaves = self.graph.vs.select(_degree=1)
        self.graph.delete_vertices(leaves)

    def plotTree(self):
        layout = self.graph.layout("rt")
        plot(self.graph, layout=layout)

    def plotMST(self):
        minTree = self.graph.spanning_tree()
        plot(minTree)

    def getVertexCount(self):
        return len(self.graph.vs["label"])




