
from Player import *
from Tree import *

class GoldGrabbingGame:

    def __init__(self):
        self.playerCount = 0
        self.players = []


    def getUserInputs(self):
        self.playerCount = int(input("Please enter number of players: "))


    def initiatePlayers(self):
        for i in range(self.playerCount):
            player = Player()
            player.setName(str("Player %d" %i))
            self.players.append(player)

    def initiateTree(self):
        vertices = int(input("Enter the number of vertices for the game tree: "))
        bFactor = int(input("Enter the branching fator of the tree: "))
        gameTree = Tree(vertices, bFactor)
        return gameTree


    def getPlayers(self):
        return(self.players)

    def rotatePlayers(self):
        element0 = self.players.pop(0)
        self.players.append(element0)


    def game(self, tree):
        while True:
            if tree.getVertexCount()<= 0:
                break
            leaves = tree.getLeaves()
            tree.plotTree()
            print("leaves: ", leaves)
            tree.deleteLeaves()
            while len(leaves) > 0:
                for i in range (len(self.players)):
                    player = self.players[0]
                    if len(leaves) > 0:
                        print("%s playing now" %player.getName())
                        player.buyVertexGreedy(leaves)
                        self.rotatePlayers()

    def getResults(self):
        for player in self.players:
            print("%s : %d" %(player.getName(), player.calculatePoints()))



    def startGame(self):
        try:
            self.getUserInputs()
        except:
            print("Please enter an integer for player count!!!!")
        finally:
            self.initiatePlayers()
            self.getPlayers()
            gameTree = self.initiateTree()
            self.game(gameTree)
            print("\n ___________________RESULTS____________________________\n")
            self.getResults()


