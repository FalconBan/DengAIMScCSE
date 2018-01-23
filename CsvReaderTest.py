'''
Created on Jan 18, 2018

@author: chaparangan
'''
import unittest
import csv
from Actions import CsvReader

fileName = "TestFile.csv"

class Test(unittest.TestCase):
    def test_CsvReader(self):
        with open(fileName, "w") as file:
            writer = csv.writer(file, delimiter=',')
            
            data = ["first_name,last_name,city".split(","),
            "Tyrese,Hirthe,Strackeport".split(","),
            "Jules,Dicki,Lake Nickolasville".split(","),
            "Dedric,Medhurst,Stiedemannberg".split(",")
            ]
            
            print(data)
            
            for line in data:
                writer.writerow(line)

        csvReader = CsvReader.CsvReader(fileName)
        csvReader.readFile()
        
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()