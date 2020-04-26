
from Player import *
from Tree import *

class GoldGrabbingGame:

    def __init__(self):
        self.playerCount = 0
        self.players = []

    def setPlayerCount(self, playerCount):
        self.playerCount = playerCount

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

    def initiateTreeByGUI(self, vertices, bFactor):
        gameTree = Tree(vertices, bFactor)
        return gameTree


    def getPlayers(self):
        return(self.players)

    def rotatePlayers(self):
        element0 = self.players.pop(0)
        self.players.append(element0)


    def game(self, tree):
        while True:
            print(tree.getVertexCount())
            if tree.getVertexCount()<= 0:
                break
            elif tree.getVertexCount() == 1:
                player = self.players[0]
                leaves = tree.getLastNode()
                print("%s playing now" % player.getName())
                player.buyVertexGreedy(leaves)
                break
            else:
                leaves = tree.getLeaves()
                tree.plotTree()
                print("leaves: ", leaves)
                tree.deleteLeaves()
                while len(leaves) > 0:
                    for i in range (len(self.players)):
                        if len(leaves) > 0:
                            player = self.players[0]
                            print("%s playing now" %player.getName())
                            player.buyVertexGreedy(leaves)
                            self.rotatePlayers()
                        else:
                            break

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


    def startGameByGUI(self, players, vertices, bFactor):
        self.setPlayerCount(players)
        self.initiatePlayers()
        gameTree = self.initiateTreeByGUI(vertices, bFactor)
        self.game(gameTree)
        print("\n ___________________RESULTS____________________________\n")
        self.getResults()


