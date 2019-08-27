'''
Created on Feb 15, 2019

@author: code
'''
import os


class Files(object):

    def readFile(self, linesToRead: int = None):
        try:
            with open(self.fileName, "r", encoding="utf8") as file:
                if linesToRead is not None:
                    return ''.join(list(file)[:linesToRead])
                else:
                    return file.read()
        except FileNotFoundError as e:
            return "Error, File not found: " + self.fileName + ". Exception: " + str(e)
        except UnicodeDecodeError as e:
            try:
                with open(self.fileName, "r", encoding="ISO-8859-1") as file:
                    if linesToRead is not None:
                        return ''.join(list(file)[:linesToRead])
                    else:
                        return file.read()
            except Exception as e:
                raise Exception
        except Exception as e:
            return "Error reading file: " + self.fileName + ". Exception: " + str(type(e)) + ": " + str(e)

    def writeFile(self, data: str, isNewFile: bool = None):
        try:
            if isNewFile is not None:
                if isNewFile is True:
                    with open(self.fileName, "x", encoding="utf8") as file:
                        file.write(data)
                elif isNewFile is False:
                    with open(self.fileName, "w", encoding="utf8") as file:
                        file.write(data)
                else:
                    return "Invalid isNewFile Parameter Passed [" + isNewFile + "]. Valid values: True or False"
            else:
                with open(self.fileName, "w", encoding="utf8") as file:
                    file.write(data)
        except FileExistsError as e:
            return "Error, file already exists: " + self.fileName + ". Exception: " + str(e)
        except FileNotFoundError as e:
            return "Error reading file: " + self.fileName + ". Exception: " + str(e)
        except Exception as e:
            return "Error writing file: " + self.fileName + ". Exception: " + str(type(e)) + ": " + str(e)

    def appendFile(self, data: str):
        try:
            with open(self.fileName, "a", encoding="utf8") as file:
                file.write(data)
        except FileExistsError as e:
            return "Error, file already exists: " + self.fileName + ". Exception: " + str(e)
        except FileNotFoundError as e:
            return "Error reading file: " + self.fileName + ". Exception: " + str(e)
        except Exception as e:
            return "Error writing file: " + self.fileName + ". Exception: " + str(type(e)) + ": " + str(e)

    def deleteFile(self):
        try:
            if os.path.exists(self.fileName):
                os.remove(self.fileName)
            else:
                return "File does not exist. " + self.fileName
        except FileExistsError as e:
            return "Error, file already exists: " + self.fileName + ". Exception: " + str(e)
        except FileNotFoundError as e:
            return "Error reading file: " + self.fileName + ". Exception: " + str(e)
        except Exception as e:
            return "Error writing file: " + self.fileName + ". Exception: " + str(type(e)) + ": " + str(e)
        finally:
            os.close()

    def __init__(self, filePath: str):
        '''
        Constructor
        '''
        if filePath is not None:
            self.fileName = filePath
        else:
            raise EOFError("Need File Path")
