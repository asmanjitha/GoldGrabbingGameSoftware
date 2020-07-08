from Tree import *
from Player import *
import os


class BulkGame:

    def __init__(self, playerCount, vertices, bFactor, id):
        self.playerCount = playerCount
        self.vertices = vertices
        self.bFactor = bFactor
        self.players = []
        self.id = id

        self.results = {}

        # directory = str(max([int(i) for i in os.listdir("Plottings")]) + 1)
        # print(directory)
        # if not os.path.exists('Plottings/' + str(directory)):
        #     os.makedirs('Plottings/' + str(directory))
        # self.root = "Plottings/" + str(directory)

    def setPlayerCount(self, playerCount):
        self.playerCount = playerCount

    def initiatePlayers(self):
        for i in range(self.playerCount):
            player = Player()
            player.setName(str("Player %d" % i))
            self.players.append(player)

    def initiateTree(self):
        gameTree = Tree(self.vertices, self.bFactor)
        # gameTree.plotTree(self.root)
        return gameTree

    def getPlayers(self):
        return (self.players)

    def rotatePlayers(self):
        element0 = self.players.pop(0)
        self.players.append(element0)

    def bulkGame(self, tree):
        while True:
            if tree.getVertexCount() <= 0:
                break
            else:
                player = self.players[0]
                player.playGreedy(tree)
                self.rotatePlayers()

    def getResults(self):
        for player in self.players:
            self.results.update({player: player.calculatePoints()})
        return self.results

    def startBulkGame(self):
        self.initiatePlayers()
        gameTree = self.initiateTree()
        self.bulkGame(gameTree)

    def getWinner(self):
        winner = None
        winningPoints = 0
        for player in self.players:
            if player.calculatePoints() > winningPoints:
                winningPoints = player.calculatePoints()
                winner = player
        return ({winner.getName(): winningPoints})
