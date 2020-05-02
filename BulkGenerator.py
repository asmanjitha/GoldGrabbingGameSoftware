
from BulkGame import *
import os


class BulkGenerator:
    def __init__(self):

        self.treeCount = int(input("Enter the number of games shoul be played: "))
        self.playerCount = int(input("Enter the number of players in each game: "))
        self.vertices = int(input("Enter the number of vertices for each game tree : "))
        self.bFactor = int(input("Enter the branching factor for each tree: "))
        self.games = []

        if not os.path.exists('Plottings'):
            os.makedirs('Plottings')




    def playGames(self):
        for i in range(self.treeCount):
            game = BulkGame(self.playerCount, self.vertices, self.bFactor ,i)
            self.games.append(game)
        for game in self.games:
            game.startBulkGame()

        for game in self.games:
            winner = game.getWinner()
            print(winner)





