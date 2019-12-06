import json

class JsonParser(object):
    def stringToJson(self, jsonString: str = None):
        try:
            if jsonString is None:
                raise Exception("Need valid JSON String to convert to JSON Object")
            else:
                self.jsObject = json.loads(jsonString)
                return self.jsObject
        except Exception as e:
            return "Invalid string passed. " + str(jsonString is not None if jsonString else "None") + ". Exception: " \
                   + str(type(e)) + ": " + str(e)

    def createJsonArray(jsonString: str = None):
        try:
            if jsonString is None:
                raise Exception("Need valid JSON String to append to JSON Array")
            else:
                js: json = {}
                return json.loads(jsonString)
        except Exception as e:
            return "Invalid string passed. " + (jsonString is not None if jsonString else "None") + ". Exception: " \
                   + str(type(e)) + ": " + str(e)

    # def toString(self):
    #     return self.jsonObject.__str__()

    def __init__(self):
        self.jsObject: json = {}
        # self.jsonObject: json = {}
        pass
