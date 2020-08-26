#
#
#
# from igraph import *
#
# def deleteLeaves(g):
#     for idx, v in enumerate(g.vs):
#         print(v["label"], v.degree())
#         if v.degree() <= 1:
#             g.delete_vertices(idx)
#
# def delete(g):
#     leaves = g.vs.select(_degree=1)
#     g.delete_vertices(leaves)
#
# def getLeaves(g):
#     leaves = g.vs.select(_degree=1)["label"]
#     return leaves
#
# g = Graph.Tree(6,3)
# g.vs["label"] = [1,2,3,4,5,6]
#
# print(VertexSeq(g))
#
# # layout = g.layout("rt")
#
# # plot(g, layout=layout)
# plot(g)
# # print(getLeaves(g))
# delete(g)
#
# # plot(g, layout=layout)
# plot(g)


gui = input("Press Enter")


