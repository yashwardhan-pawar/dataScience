import json

import pandas as pd

from DataCleaning import JSONToDataFrame as jtdf
from utilityPackage import StringBuilder as sb

businessFile = open('../Data/Yelp_DataSet/business.json', encoding='utf8')
reviewFile = open('../Data/Yelp_DataSet/review.json', encoding='utf8')
checkinFile = open('../Data/Yelp_DataSet/checkin.json', encoding='utf8')
tipFile = open('../Data/Yelp_DataSet/tip.json', encoding='utf8')
photoFile = open('../Data/Yelp_DataSet/photo.json', encoding='utf8')
userFile = open('../Data/Yelp_DataSet/user.json', encoding='utf8')

lines = businessFile.readlines()

jtdf.readJSON(lines, breakAfterLine=None)

exit(3)

columns = ['business_id', 'name', 'address', 'city', 'state', 'postal_code', 'latitude', 'longitude', 'stars',
           'review_count', 'is_open', 'attributes_GoodForKids', 'categories', 'hours']
data = pd.DataFrame(columns=columns)

fileString = sb.StringBuilder('{ "json": [')
i = 0
for line in file:
    jsonContent = json.loads(line)
    print(jsonContent)

    attr = 'None'

    if 'attributes' in jsonContent and jsonContent['attributes'] is not None:
        for key, value in jsonContent['attributes'].items():
            if value is not None:
                attr = value

    json_data = pd.DataFrame([[jsonContent['business_id'], jsonContent['name'], jsonContent['address'],
                               jsonContent['city'], jsonContent['state'], jsonContent['postal_code'],
                               jsonContent['latitude'], jsonContent['longitude'], jsonContent['stars'],
                               jsonContent['review_count'], jsonContent['is_open'], str(value),
                               jsonContent['categories'], jsonContent['hours']]])
    data = data.append(json_data)
    i += 1
    fileString.append(line + ',')
    if i > 500:
        break

data.to_pickle('yelp_pandas')
exit(3)

fileString.removeTrailingChar()
fileString.append(']}')

print('Exit')
file.close()

jsonFile = json.loads(fileString.toString())
# jsonFile.
print(jsonFile)
