import json


class JsonParser(object):

    def stringToJson(self, jsonString: str = None):
        try:
            if jsonString is None:
                raise Exception("Need valid JSON String to convert to JSON Object")
            else:
                self.jsonObject = json.loads(jsonString)
        except Exception as e:
            return "Invalid string passed. " + jsonString + ". Exception: " + str(type(e)) + ": " + str(e)

    def appendToJsonArray(self, jsonString: str = None):
        try:
            if jsonString is None:
                raise Exception("Need valid JSON String to append to JSON Array")
            else:
                self.jsonObject = json.loads(jsonString)
        except Exception as e:
            return "Invalid string passed. " + jsonString + ". Exception: " + str(type(e)) + ": " + str(e)

    def __init__(self):
        self.jsonObject = json.loads('{}')