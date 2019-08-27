from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
import nltk.collocations
from nltk.corpus import wordnet as wc
from nltk.wsd import lesk
from string import punctuation
from utilityPackage import FileUtility as fl, StringBuilder as sb

from nltk.stem.lancaster import LancasterStemmer

import pandas as pd


# print(fl.readFile('C:/Users/Dell Inspiron/PycharmProjects/DataScience/Data/data_twitter.csv'))

# Read CSV into Dataframe DF
def readcsvtodf(fileName: str = None, columns=None, numberOfRows=None):
    if columns is None:
        columns = ['target', 'id', 'date', 'flag', 'user', 'text']
    if fileName is None:
        fileName = 'C:/Users/Dell Inspiron/PycharmProjects/DataScience/Data/data_twitter.csv'
    if numberOfRows is None:
        numberOfRows = 1000
    return pd.read_csv(fileName, names=columns, nrows=numberOfRows)


# Create a paragraph from all the selected rows ('text') in DF
def textBuilder(dataFrame):
    text = sb.StringBuilder()
    for row in dataFrame.iterrows():
        text.append(row[1]['text'])
    return text.toString()


# Tokenize Sentence in the paragraph
def getSentences(text):
    return sent_tokenize(text)


# Tokenize Words in the paragraph
def getWordList(sentences):
    wordList = []
    for eachSentence in sentences:
        wordList.append(word_tokenize(eachSentence))
    return wordList


# Remove stopwords  like .,; from words list
#     Create List of Stopwords
def removeStopWords(wordList):
    try:
        customStopWordsList = set(stopwords.words('english') + list(punctuation))
        # Filter Stop Words
        filterWords = []
        for words in wordList:
            filterWords.append([word for word in words if word not in customStopWordsList])
    except:
        pass
    return filterWords


# In each sentence, find bi-grams
# bigram_measures = nltk.collocations.BigramAssocMeasures()

finder = []
#   Create Finder List & Print

dataFr = readcsvtodf(numberOfRows=9)
text = textBuilder(dataFr)
sentences = getSentences(text)
wordList = getWordList(sentences)
filterWords = removeStopWords(wordList)
for each in filterWords:
    finder.append(nltk.collocations.BigramCollocationFinder.from_words(each))

for finderBiGram in finder:
    sorted(finderBiGram.ngram_fd.items())

# Stem words and Part Of Speech
stemWords = []
partOfSpeechWords = []
lc = LancasterStemmer()
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
            sensel = lesk(word_tokenize(sentence), noun)
            if sensel is not None:
                print(noun, sentence)
                print(sensel, sensel.definition())
                print('=======================')
    for verb in listVerbs:
        if verb in sentence:
            sensel = lesk(word_tokenize(sentence), verb)
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
