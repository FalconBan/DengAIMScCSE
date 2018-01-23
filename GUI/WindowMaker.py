import tkinter as tk
from tkinter import ttk

class WindowMaker():
    def __init__(self, title):
        self.window = tk.Tk()
        self.window.title(title)
        self.window.resizable(width=0, height=0)
        self.buttonList = []
        pass
    
    def createWindow(self):
        self.window.mainloop()
        pass

    def addLabel(self, label, Row, Col):
        self.label = ttk.Label(self.window, text=label)
        self.label.grid(row=Row, column=Col)
        
    def addButton(self, label, Row, Col, onClick):
        button = ttk.Button(self.window, text=label, command=onClick)
        button.grid(row=Row, column=Col)
        self.buttonList.append(button)
       
    def addTextBox(self, Row, Col): 
        text = tk.StringVar()
        textBox = ttk.Entry(self.window, width=50, textvariable=text)
        textBox.grid(row=Row, column=Col)