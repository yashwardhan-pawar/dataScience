import nltk.collocations
from nltk.corpus import wordnet as wc
from nltk.wsd import lesk
from nltk.stem.lancaster import LancasterStemmer
from utilityPackage import FileUtility as fu
from jsonProcessor import JsonParser as jp
from utilityPackage import IntegerUtility as iu
from naturalLanguageProcessing import textTokenizer as txtLib
import json
import copy

l1 = [1,2,3]
l2 = l1
print(id(l1), id(l2))
print(l1,l2)
l3 = copy.copy(l2)
print(id(l3), l3)
l4 = copy.deepcopy(l2)
print(id(l4), l4)


def sf(a):
    print('a:', a)
    print('a%3:', a%3)
    print('a%5:', a%5)
    return a%3!=0 and a%5!=0

m=filter(sf, range(1,31))
print('+++++++++++++++++++++++++++++++++++++')
print('******** M:',  m , '*********')
print(m.__class__)
print(list(m))
print(len(list(m)))

count = {}
count[(1,2,4)] = 5
count[(4,2,1)] = 7
count[(1,2)] = 6
count[(4,2,1)] = 2
print(count)
tot = 0
for i in count:
    tot = tot + count[i]
    print('for i', i, 'and value:', count[i], 'tot = ', tot)

print('length', len(count))
print('Count', count)
print(len(count)+tot)

exit(1)

i = 5

while True:
    print(i)
    print('Value', i%0O10)
    print('Value2', 0O10)
    if i%0O10 == 0:
        break
        print(i)
    i += 1

x = (i for i in range(3))
print('x', x)
for i in x:
    print('In', i)

print('Again X', x)

for i in x:
    print('Out', i)

exit(-1)
# print(fl.readFile('C:/Users/Dell Inspiron/PycharmProjects/DataScience/Data/data_twitter.csv'))
# columns = ['target', 'id', 'date', 'flag', 'user', 'text']
# fileName = 'C:/Users/Dell Inspiron/PycharmProjects/DataScience/Data/data_twitter.csv'

file = fu.Files('C:/Users/Dell Inspiron/PycharmProjects/DataScience/Data/user.json')
# file = fu.Files('C:/Users/Dell Inspiron/PycharmProjects/DataScience/Data/data_twitter.csv')

print(file.readFile(10))
lines = file.readFile(1)

print(lines)
js = jp.JsonParser.stringToJson(lines)
print(js)

exit(-1)
#
# js = jp.JsonParser
# print(js)
# print(js.jsObject)
# for line in lines[1]:
#     unit = iu.IntegerUtility(line)
#     print(unit.isIntOrFloat())
#     js.stringToJson(None, line)
#
# print(js.toString())
# print(lines)


# for line in lines:
#     print(line)

# i = 0
# for lines in file.readFile(10):
#     if i is 15:
#         break
#     print(lines)
#     i += 1

tt = txtLib.textParser()

dataFr = tt.readCSVtoDF(columns=['target', 'id', 'date', 'flag', 'user', 'text'],
                        fileName='C:/Users/Dell Inspiron/PycharmProjects/DataScience/Data/data_twitter.csv',
                        numberOfRows=9)
text = tt.textBuilder(dataFr)
sentences = tt.getSentences(text)
wordList = tt.getWordList(sentences)
filterWords = tt.removeStopWords(wordList)

# In each sentence, find bi-grams
# bigram_measures = nltk.collocations.BigramAssocMeasures()

finder = []
#   Create Finder List & Print
for each in filterWords:
    finder.append(nltk.collocations.BigramCollocationFinder.from_words(each))

for finderBiGram in finder:
    sorted(finderBiGram.ngram_fd.items())

# Stem words and Part Of Speech
stemWords = []
partOfSpeechWords = []
lc = nltk.LancasterStemmer()
for words in filterWords:
    stemWords.append([lc.stem(word) for word in words])
    partOfSpeechWords.append(nltk.pos_tag(words))

# print('=======================')

listNouns = []
listVerbs = []
for words in partOfSpeechWords:
    for word in words:
        if 'NN' in word[1]:
            if word[0].lower() not in listNouns:
                listNouns.append(word[0].lower())
        if 'VB' in word[1]:
            if word[0].lower() not in listVerbs:
                listVerbs.append(word[0].lower())

# Disambiguating Word Meanings
#   Dictionary
for noun in listNouns:
    for ss in wc.synsets(noun):
        break
        # print(ss, ss.definition())

for verb in listVerbs:
    for ss in wc.synsets(verb):
        break
        # print(ss, ss.definition())

    #   Meaning (Using LESK Algorithm)
for sentence in sentences:
    for noun in listNouns:
        if noun in sentence:
            sensel = lesk(nltk.word_tokenize(sentence), noun)
            if sensel is not None:
                print(noun, sentence)
                print(sensel, sensel.definition())
                print('=======================')
    for verb in listVerbs:
        if verb in sentence:
            sensel = lesk(nltk.word_tokenize(sentence), verb)
            if sensel is not None:
                print(verb, sentence)
                print(sensel, sensel.definition())
                print('=======================')

########################################################################################################################
#                               TWITTER SENTIMENT ANALYSIS                                                             #
########################################################################################################################
from nltk.probability import FreqDist

freqWords = []
for sente in filterWords:
    for word in sente:
        freqWords.append(word)

freq = FreqDist(freqWords)
print(freq.plot())
