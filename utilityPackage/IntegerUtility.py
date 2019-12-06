'''
Created on Feb 15, 2019

@author: code
'''


class IntegerUtility(object):
    def isIntOrFloat(self):
        if isinstance(self.testObject, int):
            return True
        else:
            try:
                int(self.testObject)
                return True
            except Exception as e:
                try:
                    float(self.testObject)
                    return True
                except Exception as e:
                    return False

    def isInt(self):
        if isinstance(self.testObject, int):
            return True
        else:
            try:
                int(self.testObject)
                return True
            except Exception as e:
                return False

    def isFloat(self):
        if isinstance(self.testObject, float):
            return True
        else:
            try:
                float(self.testObject)
                return True
            except Exception as e:
                return False

    def __init__(self, testObject):
        '''
        Constructor
        '''
        self.testObject = testObject
