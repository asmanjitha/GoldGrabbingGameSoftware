from BulkGame import *
import os


class BulkGenerator:
    def __init__(self):

        # self.treeCount = int(input("Enter the number of games shoul be played: "))
        # self.playerCount = int(input("Enter the number of players in each game: "))
        # self.vertices = int(input("Enter the number of vertices for each game tree : "))
        # self.bFactor = int(input("Enter the branching factor for each tree: "))
        self.treeCount = 100
        self.playerCount = 2
        self.vertices = 10
        self.bFactor = 2
        self.games = []
        self.winners = []

        if not os.path.exists('Plottings'):
            os.makedirs('Plottings')


    def getUserData(self):
        self.treeCount = int(input("Enter the number of games shoul be played: "))
        self.playerCount = int(input("Enter the number of players in each game: "))
        self.vertices = int(input("Enter the number of vertices for each game tree : "))
        self.bFactor = int(input("Enter the branching factor for each tree: "))

    def startByGUI(self, treeCount, playerCount, vertices, bFactor):
        self.treeCount = treeCount
        self.playerCount = playerCount
        self.vertices = vertices
        self.bFactor = bFactor
        self.playGames()

    def calculateProbabilities(self):
        playersWinnigData = {}
        for i in range(self.playerCount):
            name = "Player %d" % i
            playersWinnigData[name] = 0
        for winner in self.winners:
            for key in winner.keys():
                playersWinnigData[key] += 1
        self.summary(playersWinnigData)

    def summary(self, playersWinnigData):
        print("\n ============================================RESULTS====================================\n")
        print("Number of games played : %d" % self.treeCount)
        print("Number of players played in each game : %d" % self.playerCount)
        print("Number of vertices in each game tree : %d" % self.vertices)
        print("Branching factor of each game tree : %d" % self.bFactor)

        print("\nNumber of games won by each player : ")
        for key in playersWinnigData.keys():
            print(key + " : ", str(playersWinnigData[key]) + " Games")
        print("\nWinning Probabilities : ")
        for key in playersWinnigData.keys():
            print(key + " : ", str(playersWinnigData[key] / self.treeCount * 100) + "%")

    def playGames(self):
        for i in range(self.treeCount):
            game = BulkGame(self.playerCount, self.vertices, self.bFactor, i)
            self.games.append(game)
        for game in self.games:
            game.startBulkGame()

        for game in self.games:
            winner = game.getWinner()
            self.winners.append(winner)
            # print(winner)
        self.calculateProbabilities()
