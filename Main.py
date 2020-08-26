from GoldGrabbingGame import *
from BulkGenerator import *

if __name__ == '__main__':
    print("Starting.....")
    # game = GoldGrabbingGame()
    # game.startSingleGame()

    generator = BulkGenerator()
    generator.getUserData()
    generator.playGames()
    # generator.startByGUI(10,2,10,2)
    # input("Press enter to exit")
