import tkinter as tk
from BulkGenerator import *

window = tk.Tk()
window.title("Gold Grabbing Game")


# ===========================METHODS===============================================

def startGame():
    print("Starting Game.....")
    try:
        games = int(gamesNumberentry.get())
        players = int(playersNumberentry.get())
        vertices = int(verticesNumberentry.get())
        bFactor = int(branchingFactorEntry.get())

        if games > 1000:
            print("!!! Please enter a value less than 1000 for number of games!!!")
        elif players > 3:
            print("!!! Please enter a value less than or equals 3 for number of players!!!")
        elif vertices > 50:
            print("!!! Please enter a value less than 50 for number of vertices!!!")
        elif bFactor > 5:
            print("!!! Please enter a value less than 5 for branching factor!!!")
        else:
            # button['state'] = tk.DISABLED
            button.pack_forget()
            generator = BulkGenerator()
            generator.startByGUI(games, players, vertices, bFactor)
    except Exception as e:
        print(e)


# ===========================EVENT HANDLER==========================================

def startGameButtonPressed(event):
    startGame()


# =========================GUI DESIGN=================================================
frameNavigator = tk.Frame()
frameNavigator.pack(fill=tk.X, ipadx=5, ipady=5)

# btn_submit = tk.Button(master=frameNavigator, text="Single Game")
# btn_submit.pack(side=tk.LEFT, padx=10, ipadx=10)
#
# btn_clear = tk.Button(master=frameNavigator, text="Multiple Games")
# btn_clear.pack(side=tk.LEFT, ipadx=10)

# -------------------TOP FRAME-----------------------------------------------------------
frameTop = tk.Frame()
label = tk.Label(
    text="Multiple Games",
    width=100,
    height=5,
    master=frameTop
)

label.pack()
frameTop.pack()

# ---------------------MIDDDLE FRAME1----------------------------------------------------
frameMiddle0 = tk.Frame()

frameMiddleLeft = tk.Frame(master=frameMiddle0)
label = tk.Label(
    text="Enter number of Games to be played: ",
    width=40,
    height=2,
    master=frameMiddleLeft
)

label.pack()
frameMiddleLeft.pack(side=tk.LEFT)

frameMiddleRight = tk.Frame(master=frameMiddle0)
gamesNumberentry = tk.Entry(
    width=20,
    master=frameMiddleRight
)
gamesNumberentry.pack()
gamesNumberentry.insert(0, 100)

frameMiddleRight.pack(side=tk.LEFT)

frameMiddle0.pack()







frameMiddle1 = tk.Frame()

frameMiddleLeft = tk.Frame(master=frameMiddle1)
label = tk.Label(
    text="Enter number of players: ",
    width=40,
    height=2,
    master=frameMiddleLeft
)

label.pack()
frameMiddleLeft.pack(side=tk.LEFT)

frameMiddleRight = tk.Frame(master=frameMiddle1)
playersNumberentry = tk.Entry(
    width=20,
    master=frameMiddleRight
)
playersNumberentry.pack()
playersNumberentry.insert(0, 2)

frameMiddleRight.pack(side=tk.LEFT)

frameMiddle1.pack()

# ---------------------MIDDDLE FRAME2----------------------------------------------------


frameMiddle2 = tk.Frame()

frameMiddleLeft = tk.Frame(master=frameMiddle2)
label = tk.Label(
    text="Enter number of vertices: ",
    width=40,
    height=2,
    master=frameMiddleLeft
)

label.pack()
frameMiddleLeft.pack(side=tk.LEFT)

frameMiddleRight = tk.Frame(master=frameMiddle2)
verticesNumberentry = tk.Entry(
    width=20,
    master=frameMiddleRight
)
verticesNumberentry.pack()
verticesNumberentry.insert(0, 10)
frameMiddleRight.pack(side=tk.LEFT)

frameMiddle2.pack()

# ---------------------MIDDDLE FRAME3----------------------------------------------------


frameMiddle3 = tk.Frame()

frameMiddleLeft = tk.Frame(master=frameMiddle3)
label = tk.Label(
    text="Enter branching factor of the tree: ",
    width=40,
    height=2,
    master=frameMiddleLeft
)

label.pack()
frameMiddleLeft.pack(side=tk.LEFT)

frameMiddleRight = tk.Frame(master=frameMiddle3)
branchingFactorEntry = tk.Entry(
    width=20,
    master=frameMiddleRight
)
branchingFactorEntry.pack()
branchingFactorEntry.insert(0, 2)
frameMiddleRight.pack(side=tk.LEFT)

frameMiddle3.pack()

# ---------------------RUN BUTTON-----------------------------------------------------------

frameRunButton = tk.Frame(borderwidth=10)
button = tk.Button(
    text="Run Game!",
    width=25,
    height=2,
    bg="#2ecc71",
    fg="black",
    master=frameRunButton
)
button.bind("<Button-1>", startGameButtonPressed)
button.pack()
frameRunButton.pack()

# ---------------------BOTTOM FRAME-----------------------------------------------------------
frameBottom = tk.Frame(borderwidth=20)
resultsText = tk.Text(
    master=frameBottom,
    width=100,
    height=1
)

resultsText.pack()

frameBottom.pack()

# ------------------------------END GUI-----------------------------------------------------------


window.mainloop()
