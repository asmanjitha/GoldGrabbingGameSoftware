import tkinter as tk
from GoldGrabbingGame import *

window = tk.Tk()
window.title("Gold Grabbing Game")

#=================Heading===============================

frameTop = tk.Frame()
label = tk.Label(
    text="Gold Grabbing Game",
    width=100,
    height=5,
    master=frameTop
)

label.pack()
frameTop.pack()

#====================Heading ENd======================================

#====================Select buttons==================================

frameButtons = tk.Frame(borderwidth=10)
button1 = tk.Button(
    text="Run Game!",
    width=25,
    height=2,
    bg="#3498db",
    fg="white",
    padx=10,
    pady=20,
    master=frameButtons
)

button2 = tk.Button(
    text="Run Game!",
    width=25,
    height=2,
    bg="#2ecc71",
    fg="white",
    padx=10,
    pady=20,
    master=frameButtons
)
# button.bind("<Button-1>", startGameButtonPressed)
button1.pack(padx=20, pady=20)
button2.pack(padx=20, pady=20)
frameButtons.pack()

#====================Select Buttins End===============================

window.mainloop()