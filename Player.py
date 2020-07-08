class Player:

    def __init__(self):
        self.name = ""
        self.points = 0
        self.vertices = []

    def buyVertexGreedy(self, leaves, tree):
        if len(leaves) > 0:
            point = 0
            maxLeaf = None;
            for leaf in leaves:
                if int(leaf["label"]) > point:
                    point = int(leaf["label"])
                    maxLeaf = leaf
            self.vertices.append(point)
            tree.deleteLeaves([maxLeaf])
            # print("%s got %d points" %(self.getName(), point) )

    def playGreedy(self, tree):
        if tree.getVertexCount() == 1:
            leaves = tree.graph.vs
            self.buyVertexGreedy(leaves, tree)
        elif tree.getVertexCount() > 1:
            leaves = tree.graph.vs.select(_degree=1)
            self.buyVertexGreedy(leaves, tree)

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def calculatePoints(self):
        self.points = sum(self.vertices)
        return self.points
