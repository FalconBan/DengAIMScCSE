'''
Created on Jan 18, 2018

@author: chaparangan
'''

from GUI import WindowMaker
from Actions import CsvReader

class DiagramDisplayer:

    def __init__(self, name):
        self.name = name
        pass
        
    def createDiagram(self):
        window = WindowMaker.WindowMaker(self.name)
        window.addLabel(self.name, 0, 0)
        window.addLabel("Diagram", 0, 1)
        window.addButton("Draw", 1, 0)
        
    def drawDiagram(self, fileName):
        window = WindowMaker.WindowMaker(self.name)
        csvReader = CsvReader.CsvReader(fileName)