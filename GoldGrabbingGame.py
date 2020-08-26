from Player import *
from Tree import *

from Logger import *


class GoldGrabbingGame:

    def __init__(self, *textBox):
        self.playerCount = 0
        self.players = []
        self.logger = Logger(textBox)
        self.gamePath = "Plottings/GoldGrabbingGame"

    def setPlayerCount(self, playerCount):
        self.playerCount = playerCount

    def getUserInputs(self):
        self.playerCount = int(input("Please enter number of players: "))

    def initiatePlayers(self):
        for i in range(self.playerCount):
            player = Player()
            player.setName(str("Player %d" % i))
            self.players.append(player)

    def initiateTree(self):
        vertices = int(input("Enter the number of vertices for the game tree: "))
        bFactor = int(input("Enter the branching fator of the tree: "))
        gameTree = Tree(vertices, bFactor)
        return gameTree

    def initiateTreeByGUI(self, vertices, bFactor):
        gameTree = Tree(vertices, bFactor)
        return gameTree

    def getPlayers(self):
        return (self.players)

    def rotatePlayers(self):
        element0 = self.players.pop(0)
        self.players.append(element0)

    def singleGame(self, tree):
        # tree.plotTree()
        while True:
            # print(tree.getVertexCount())
            if tree.getVertexCount() <= 0:
                break
            else:
                # tree.plotTree()
                player = self.players[0]
                # print("%s playing now" % player.getName())
                player.playGreedy(tree)
                self.rotatePlayers()

    def getResults(self):
        for player in self.players:
            print("%s : %d" % (player.getName(), player.calculatePoints()))

    def startSingleGame(self):
        try:
            self.getUserInputs()
        except:
            print("Please enter an integer for player count!!!!")
        finally:
            self.initiatePlayers()
            self.getPlayers()
            gameTree = self.initiateTree()
            self.singleGame(gameTree)
            print("\n ___________________RESULTS____________________________\n")
            self.getResults()

    def startGameByGUI(self, players, vertices, bFactor):
        self.setPlayerCount(players)
        self.initiatePlayers()
        gameTree = self.initiateTreeByGUI(vertices, bFactor)
        self.singleGame(gameTree)
        # self.logger.writeLine("___________________RESULTS____________________________")
        self.getResults()
