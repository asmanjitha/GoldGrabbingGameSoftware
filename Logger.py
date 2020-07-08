import tkinter as tk


class Logger:

    def __init__(self, textBox):
        self.textBox = textBox

    def writeLine(self, text):
        self.textBox.insert(tk.END, text + "\n")
