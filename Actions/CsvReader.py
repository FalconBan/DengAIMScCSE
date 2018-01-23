'''
Created on Jan 18, 2018

@author: chaparangan
'''

class CsvReader:
    def __init__(self, name):
        self.values = []
        self.name = name
        
    def readFile(self): 
        with open(self.name, "r") as file:
                        
            for line in file:
                values = line.split(',')
                if values[-1] == '\n':
                    continue
                if values[-1][-1] == '\n':
                    values[-1] = values[-1][:-1]
                self.values.append(values)
            
            print(self.values)