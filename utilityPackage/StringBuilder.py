'''
Created on Feb 15, 2019

@author: code
'''


class StringBuilder(object):
    '''
    classdocs
    '''

    def append(self, stringToAppend: str):
        self.returnString += stringToAppend

    def appendLowerCase(self, stringToAppend: str):
        self.returnString += stringToAppend.lower()

    def appendUpperCase(self, stringToAppend: str):
        self.returnString += stringToAppend.upper()

    def appendCapatalize(self, stringToAppend: str):
        self.returnString += stringToAppend.capitalize()

    def removeTrailingChar(self, index: int = None):
        if index is None or index == 0:
            self.returnString = self.returnString[:-1] 
        else:
            self.returnString = self.returnString[:-index]

    def removeStartingChar(self, index: int = None):
        if index is None or index == 0:
            self.returnString = self.returnString[1:]
        else:
            self.returnString = self.returnString[index:]
            
    def toString(self):
        return str(self.returnString)
    
    def length(self):
        return self.returnString.__len__()

    def __init__(self, initialString: str = None):
        '''
        Constructor
        '''
        if initialString is not None:
            self.returnString = initialString
        else:
            self.returnString = ""
