'''
Created on Feb 15, 2019

@author: code
'''
from typing import TextIO
import os

def readFile(fileName):
    try:
        f = open(fileName, "r")
        return f.read()
    except FileNotFoundError as e:
        return "Error, File not found: " + fileName + "Execption: " + e.errno + str(e)
    except Exception as e:
        return "Error reading file: " + fileName + "Execption: " + e.errno + str(e)


def writeFile(fileName, data, isNewFile=None):
    try:
        if isNewFile != None:
            if isNewFile == True:
                f = open(fileName, "x")
                f.write(data)
            elif isNewFile == False:
                f = open(fileName, "w")
                f.write(data)
            else:
                return "Invalid isNewFile Parameter Passed ["+isNewFile+"]. Valid values: True or False"
        else:
            f = open(fileName, "w")
            f.write(data)
    except FileExistsError as e:
        return "Error, file already exists: " + fileName + "Execption: " + e.errno + str(e)
    except FileNotFoundError as e:
        return "Error reading file: " + fileName + "Execption: " + e.errno + str(e)
    except Exception as e:
        return "Error writing file: " + fileName + "Execption: " + e.errno + str(e)

def appendFile(fileName, data):
    try:
        f = open(fileName, "a")
        f.write(data)
    except FileExistsError as e:
        return "Error, file already exists: " + fileName + "Execption: " + e.errno + str(e)
    except FileNotFoundError as e:
        return "Error reading file: " + fileName + "Execption: " + e.errno + str(e)
    except Exception as e:
        return "Error writing file: " + fileName + "Execption: " + e.errno + str(e)

def deleteFile(fileName):
    try:
        if os.path.exists(fileName):
            os.remove(fileName)
        else:
            return "File does not exist. " + fileName
    except FileExistsError as e:
        return "Error, file already exists: " + fileName + "Execption: " + e.errno + str(e)
    except FileNotFoundError as e:
        return "Error reading file: " + fileName + "Execption: " + e.errno + str(e)
    except Exception as e:
        return "Error writing file: " + fileName + "Execption: " + e.errno + str(e)