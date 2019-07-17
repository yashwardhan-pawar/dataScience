# from ../httpRequestor import httpResponse
from utilityPackage import FileUtility as fu
import re
import time
import sys
import time
from datetime import datetime
from typing import List
from utilityPackage import ArrayUtility as au


au.call_func()
sys.exit(0)


from bs4 import BeautifulSoup

from httpRequestor import httpResponse
from utilityPackage import FileUtility as fu

URL = "http://maps.googleapis.com/maps/api/geocode/json"

URL = "maps.googleapis.com/maps/api/js?key=AIzaSyAve5FCxnf78jPRs8yIaaTxsLPpU2S9UbE&callback=initialize"

# location given here
location = "delhi technological university"

# defining a params dict for the parameters to be sent to the API
PARAMS = {'address': location}

PARAMS = None

URL = "https://news.search.yahoo.com/search;_ylt=AwrC2Q6TW5RcKEIAGwjQtDMD;_ylc=X1MDNTM3MjAyNzIEX3IDMgRmcgN1aDNfbmV3c192ZXJ0X2dzBGdwcmlkAwRuX3JzbHQDMARuX3N1Z2cDMARvcmlnaW4DbmV3cy5zZWFyY2gueWFob28uY29tBHBvcwMwBHBxc3RyAwRwcXN0cmwDBHFzdHJsAzQEcXVlcnkDZ29sZAR0X3N0bXADMTU1MzIyNjc0Ng--?p=gold&fr2=sb-top-news.search&fr=uh3_news_vert_gs"
tagsName = []
tags = []
#htmlText: List[str] = []

HTTPConnectionResponse = httpResponse.httpResponseClass(URL, PARAMS)
bfsHtml = BeautifulSoup(HTTPConnectionResponse.getResponse(), 'html.parser')
fu.writeFile("HTMLPage_gold.html", bfsHtml.prettify())

for tag in bfsHtml.find_all():
    tagsName.append(tag.name)
    tags.append(str(tag))

tagsName = list(dict.fromkeys(tagsName))
tags = list(dict.fromkeys(tags))
# tags.sort()
# tagsName.sort()

for name in tagsName:
    if name in ["a", "div", "h3", "ol"]:
        # print(" =================================================================================================== ")
        # print("Getting Text for Tag: " + name)
        for text in bfsHtml.find_all(name):
            if len(text.get_text()) > 20:
                # print(text.get_text())
                htmlText.append(text.get_text())

# print (htmlText.__len__())
# htmlText = list(dict.fromkeys(htmlText))
# print (htmlText.__len__())

for num in range(1, 28):
    URL = "https://news.search.yahoo.com/search;_ylt=AwrC1DFnW5RcpSAAUmrQtDMD;_ylu=X3oDMTEzajVvczlrBGNvbG8DYmYxBHBvcwMxBHZ0aWQDBHNlYwNwYWdpbmF0aW9u?p=gold&pz=10&fr=uh3_news_vert_gs&fr2=p%3Anews%2Cm%3Asb&bct=0&b=" + str(
        (num * 10) + 1) + "&pz=10&bct=0&xargs=0"
    HTTPConnectionResponse = httpResponse.httpResponseClass(URL, PARAMS)
    bfsHtml = BeautifulSoup(HTTPConnectionResponse.getResponse(), 'html.parser')
    fu.appendFile("HTMLPage_gold.html", bfsHtml.prettify())
    print(str(datetime.now()) + " Going to sleep for 30 sec. Iteration: " + str(num))
    time.sleep(3)
    for name in ["a", "div", "h3", "ol"]:
        for text in bfsHtml.find_all(name):
            if len(text.get_text()) > 20:
                # print(text.get_text())
                htmlText.append(text.get_text())

print (htmlText.__len__())
htmlText = list(dict.fromkeys(htmlText))
print (htmlText.__len__())

fu.writeFile("HTMLParsing_gold.txt", '\n'.join(htmlText))

sys.exit(0)

print(tags)
tagsName = tags.name
tagsList = list(dict.fromkeys(tagsName))

for tag in tagsList:
    print(tag.name)

sys.exit(0)

for tag in bfsHtml.find_all():
    print(str(tag))
    print(tag.name)
    for text in bfsHtml.find_all(tag.name):
        print(text.get_text())

sys.exit(-1)

for link in bfsHtml.findAll('a'):
    # print(link.get('href'))
    # print(link.get_text())
    print("Exit A")

for link in bfsHtml.findAll('p'):
    # print(link.get('href'))
    print(link.get_text())

for link in bfsHtml.findAll('p'):
    # print(link.get('href'))
    print(link.get_text())

sys.exit(-1)

tag = list(bfsHtml.find_all("a"))
print(tag.__len__())
print(tag[5].get_text())
htmlPage = list(bfsHtml.children)[1]
htmlPage = list(htmlPage.children)[1]
# htmlPage = list(htmlPage.children)[4]
htmlPage = list(htmlPage.children)[4]
htmlPage = list(htmlPage.children)[3]
htmlPage = list(htmlPage.children)[1]
htmlPage = list(htmlPage.children)[1]
print(htmlPage)
print("All Src")
tag = list(htmlPage.find_all("a"))
print(tag.__len__())
print(tag[1].get_text())

for link in htmlPage.findAll('a'):
    # print(link.get('href'))
    print(link.get_text())

sys.exit(-1)

print(list(htmlPage.children).__len__())
print(list(htmlPage.children)[1])
print(BeautifulSoup(list(htmlPage.children)[1], 'html.parser').HTML_FORMATTERS)
# print(bfsHtml.prettify())
bfs = bfsHtml.handle_data(data2)
# print(bfs)

# extracting latitude, longitude and formatted address
# of the first matching location
latitude = data['results'][0]['geometry']['location']['lat']
longitude = data['results'][0]['geometry']['location']['lng']
formatted_address = data['results'][0]['formatted_address']

# printing the output
print("Latitude:%s\nLongitude:%s\nFormatted Address:%s" % (latitude, longitude, formatted_address))

print(httpResponse(URL))
