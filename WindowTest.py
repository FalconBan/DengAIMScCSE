'''
Created on Jan 9, 2018

@author: chaparangan
'''
import unittest
from GUI import WindowMaker

class Test(unittest.TestCase):

    def test_WindowMaker(self):
        windowMaker = WindowMaker.WindowMaker("Test Window")
        windowMaker.addLabel("Test label", 0, 0)
        windowMaker.addButton("Test Button", 1, 1, None)
        windowMaker.addTextBox(1, 0)
        windowMaker.createWindow()

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()