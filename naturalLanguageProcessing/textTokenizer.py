from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords

from string import punctuation
from utilityPackage import FileUtility as fl, StringBuilder as sb
from Exception import UserException

import pandas as pd


class textParser(object):

    # Read CSV into Dataframe DF
    def readCSVtoDF(self, fileName: str = None, columns=None, numberOfRows=None):
        try:
            if columns is None:
                raise UserException('Error! No column passed', columns)
            if fileName is None:
                raise UserException('Error! No filePath/fileName passed', fileName)
            if numberOfRows is None:
                numberOfRows = 1000
            return pd.read_csv(fileName, names=columns, nrows=numberOfRows)
        except Exception as e:
            print('Exception occurred while storing CSV to dataframe. Error:', str(e))

    # Create a paragraph from all the selected rows ('text') in DF
    def textBuilder(self, dataFrame):
        text = sb.StringBuilder()
        try:
            for row in dataFrame.iterrows():
                text.append(row[1]['text'])
        except Exception as e:
            print('Exception occurred while building text from dataframe. Error:', str(e))
            pass
        return text.toString()

    # Tokenize Sentence in the paragraph
    def getSentences(self, text):
        return sent_tokenize(text)

    # Tokenize Words in the sentences
    def getWordList(self, sentences):
        wordList = []
        try:
            for eachSentence in sentences:
                wordList.append(word_tokenize(eachSentence))
        except Exception as e:
            print('Exception occurred while getting list of words from sentences. Error:', str(e))
            pass
        return wordList

    # Remove stopwords  like .,; from words list
    #     Create List of Stopwords
    def removeStopWords(self, wordList):
        try:
            customStopWordsList = set(stopwords.words('english') + list(punctuation))
            # Filter Stop Words
            filterWords = []
            for words in wordList:
                filterWords.append([word for word in words if word not in customStopWordsList])
        except Exception as e:
            print('Exception occurred while removing stop words. Error:', str(e))
            pass
        return filterWords


