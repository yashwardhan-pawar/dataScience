'''
Created on Feb 15, 2019

@author: code
'''

class MyClass(object):
    '''
    classdocs
    '''
    
    def isInt(self, testObject):
        if isinstance(testObject, int):
            return True
        else:
            try:
                testObject = int(testObject)
                return True
            except:
                return False     


    def __init__(self):
        '''
        Constructor
        '''