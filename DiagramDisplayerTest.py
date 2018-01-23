'''
Created on Jan 18, 2018

@author: chaparangan
'''
import unittest
from Actions import DiagramDisplayer
from GUI import WindowMaker

class Test(unittest.TestCase):
    def test_DiagramDisplayer(self):
        diagramDisplayer = DiagramDisplayer.DiagramDisplayer("DiagramDisplayer")
        windowMaker = WindowMaker.WindowMaker("Test Window")
        windowMaker.addLabel("Test label", 0, 0)
        windowMaker.addButton("Test Button", 0, 1, diagramDisplayer.createDiagram)
        windowMaker.createWindow()


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_DiagramDisplayer']
    unittest.main()