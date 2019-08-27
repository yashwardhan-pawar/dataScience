'''

'''
import json


def readJSON(lines, JSONkey: str = None, level: int = None, breakAfterLine: int = None):
    primaryKeys: list = []
    secondaryKeys: list = []
    iteratorList: list = []
    i: int = 0
    if level is None:
        level = 1
    for line in lines:
        if breakAfterLine is not None:
            if i >= breakAfterLine:
                break
        i += 1
        JSON = json.loads(line)

        if JSONkey is None:
            for key in JSON:
                if isinstance(JSON[key], dict) or (isinstance(JSON[key], str) and JSON[key].startswith('{')):
                    if key not in secondaryKeys:
                        secondaryKeys.append(key)
                else:
                    if key not in primaryKeys:
                        primaryKeys.append(key)
        elif JSONkey in JSON.keys() and JSON[JSONkey] is not None:
            for key in JSON[JSONkey]:
                if isinstance(JSON[JSONkey][key], dict) or (isinstance(JSON[JSONkey][key], str)
                                                            and JSON[JSONkey][key].startswith('{')):
                    if key not in secondaryKeys:
                        secondaryKeys.append(key)
                else:
                    if key not in primaryKeys:
                        primaryKeys.append(key)

    print('Total line processed: ' + str(i))
    for x in secondaryKeys:
        if x in primaryKeys:
            primaryKeys.remove(x)
    print('Primary Key: ' + str(primaryKeys))
    print('Secondary Key: ' + str(secondaryKeys))

    if secondaryKeys.__len__() > 0:
        level += 1
        iteratorList = secondaryKeys
        j = 0
        while j < iteratorList.__len__():
            print('Iterating for key [' + iteratorList[j] + '], Level: ' + str(level))
            readJSON(lines, iteratorList[j], level, breakAfterLine)
            j += 1
    else:
        iteratorList.clear()
