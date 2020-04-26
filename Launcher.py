from igraph import *
import plotly.graph_objects as go

class Launcher:

    def __init__(self):
        self.players = 0
        self.height = 0
        self.bFactor = 0
        self.vertices = 0
        self.edges = 0
        self.labels = []
        self.M = 0
        self.position = []


    def getUserInputs(self):
        self.players = int(input("Please input the number of players: "))
        self.height = int(input("Please input the maximum height: "))
        self.bFactor = int(input("Please input the branching factor of the tree: "))
        self.vertices = int(input("Please input NUMBER OF VERTICES: "))
        self.edges = int(input("Please input number of edges: "))

    def printValues(self):
        print("PLayers: ", self.players)
        print("Height: ", self.height)
        print("Branching Factor: ", self.bFactor)
        print("Vertices: ", self.vertices)


    def generateGraph(self):
        g = Graph()
        g.add_vertices(self.vertices)
        print()
        edges = []
        print("Enter all edges: \n")
        for i in range(self.edges):
            head = int(input("\t head of edge %d :" %i))
            tail = int(input("\t tail of edge %d :" %i))
            edge = (head, tail)
            edges.append(edge)
        print(edges)
        g.add_edges(edges)
        print(g)
        # print(g.get_eid(0,1))


    def generateTree(self):
        g = Graph.Tree(self.vertices, self.bFactor)
        v_label = list(map(str, range(self.vertices)))
        print("\n", summary(g))
        lay = g.layout('rt')

        position = {k: lay[k] for k in range(self.vertices)}
        Y = [lay[k][1] for k in range(self.vertices)]
        M = max(Y)

        es = EdgeSeq(g)  # sequence of edges
        E = [e.tuple for e in g.es]  # list of edges

        L = len(position)
        Xn = [position[k][0] for k in range(L)]
        Yn = [2 * M - position[k][1] for k in range(L)]
        Xe = []
        Ye = []
        for edge in E:
            Xe += [position[edge[0]][0], position[edge[1]][0], None]
            Ye += [2 * M - position[edge[0]][1], 2 * M - position[edge[1]][1], None]

        self.labels = v_label

        fig = go.Figure()
        fig.add_trace(go.Scatter(x=Xe,
                                 y=Ye,
                                 mode='lines',
                                 line=dict(color='rgb(210,210,210)', width=1),
                                 hoverinfo='none'
                                 ))
        fig.add_trace(go.Scatter(x=Xn,
                                 y=Yn,
                                 mode='markers',
                                 name='bla',
                                 marker=dict(symbol='circle-dot',
                                             size=18,
                                             color='#6175c1',  # '#DB4551',
                                             line=dict(color='rgb(50,50,50)', width=1)
                                             ),
                                 text=self.labels,
                                 hoverinfo='text',
                                 opacity=0.8
                                 ))
        fig.show()




    def main(self):
        self.getUserInputs()
        # self.printValues()
        self.generateTree()




if __name__ == '__main__':
    p = [2,5,6,4,9,5,8,6,5,3]
    point = p.pop(p.index(max(p)))
    print(point)
