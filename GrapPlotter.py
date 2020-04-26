import igraph
import random
from igraph import *
import plotly.graph_objects as go



g = Graph.Tree(20, 3)
arr = []

for i in range(100):
    val = random.randint(0,1000)
    arr.append(val)

g.vs["name"] = arr

print(g.get_edgelist())
print(g.vs["name"])
print(g.degree())

print(g.vs.select(_degree = 1)["name"])

g.vs["label"] = g.vs["name"]

for v in g.vs:
    print(v.degree())

# minTree = g.spanning_tree()
# plot(minTree)

layout = g.layout("rt")

print(len(g.vs["label"]))

# plot(g, layout = layout)


# fig = go.Figure(gata = go.)