'''
Created on Feb 15, 2019

@author: code
'''


def isIntOrFloat(self, testObject):
    if isinstance(testObject, int):
        return True
    else:
        try:
            int(testObject)
            return True
        except:
            try:
                float(testObject)
                return True
            except:
                return False


def isInt(self, testObject):
    if isinstance(testObject, int):
        return True
    else:
        try:
            int(testObject)
            return True
        except:
            return False


def isFloat(self, testObject):
    if isinstance(testObject, float):
        return True
    else:
        try:
            float(testObject)
            return True
        except:
            return False
