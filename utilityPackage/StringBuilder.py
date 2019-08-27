'''
Created on Feb 15, 2019

@author: code
'''

'''
Use JOIN
'''


class StringBuilder(object):
    '''
    classdocs
    '''

    def _append(self, stringToAppend: str):
        return [self.returnString, stringToAppend]

    def append(self, stringToAppend: str):
        self.returnString = ''.join(self._append(stringToAppend))

    def appendLowerCase(self, stringToAppend: str):
        self.returnString = ''.join(self._append(stringToAppend.lower()))

    def appendUpperCase(self, stringToAppend: str):
        self.returnString = ''.join(self._append(stringToAppend.upper()))

    def appendCapatalize(self, stringToAppend: str):
        self.returnString = ''.join(self._append(stringToAppend.capitalize()))

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
        return len(self.returnString)

    def __init__(self, initialString: str = None):
        '''
        Constructor
        '''
        if initialString is not None:
            self.returnString = initialString
        else:
            self.returnString = ""
