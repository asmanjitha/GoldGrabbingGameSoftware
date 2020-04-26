

class Player:

    def __init__(self):
        self.name = ""
        self.points = 0
        self.vertices = []

    def buyVertexGreedy(self,leaves):
        if len(leaves) > 0:
            point = leaves.pop(leaves.index(max(leaves)))
            self.vertices.append(point)
            print("%s got %d points" %(self.getName(), point) )
        return leaves

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name


    def calculatePoints(self):
        self.points = sum(self.vertices)
        return self.points






