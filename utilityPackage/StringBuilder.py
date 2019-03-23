'''
Created on Feb 15, 2019

@author: code
'''
from setuptools.unicode_utils import try_encode
class AppendString(object):
    '''
    classdocs
    '''
    def append(self, stringToAppend):
        self.returnString += stringToAppend

    def appendLowerCase(self, stringToAppend):
        self.returnString += stringToAppend.lower()

    def appendUpperCase(self, stringToAppend):
        self.returnString += stringToAppend.upper()

    def appendCapatalize(self, stringToAppend):
        self.returnString += stringToAppend.capitalize()
        
    def removeTrailingChar(self, index=None):
        if index is None or index == 0:
            self.returnString = self.returnString[:-1] 
        else:
            self.returnString = self.returnString[:-index]
        
    def removeStartingChar(self, index=None):
        if index is None or index == 0:
            self.returnString = self.returnString[1:]
        else:
            self.returnString = self.returnString[index:]
            
    def toString(self):
        return self.returnString
    
    def length(self):
        return self.returnString.__len__()
    
    def __init__(self, initialString=None):
        '''
        Constructor
        '''
        if initialString is not None:
            self.returnString = initialString
        else:
            self.returnString = ""
