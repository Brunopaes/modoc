#!-*- coding: utf8 -*-
from __future__ import division
from sklearn.naive_bayes import MultinomialNB
import pandas
import nltk


class NLTK(object):
    def __init__(self):
        self.dataFrame = pandas.read_csv("/Users/brunopaes/Documents/OneDrive/Acadêmico/ESPM/Projetos/Microagression/data/Book1.csv", encoding="utf-8")
        self.stopwords = nltk.corpus.stopwords.words("portuguese")
        self.stemmer = nltk.stem.RSLPStemmer()
        self.xDF = self.dataFrame['microagression']
        self.yDF = self.dataFrame['class']
        self.lowerText = self.xDF.str.lower()
        self.nxDF = [nltk.tokenize.word_tokenize(i) for i in self.lowerText]
        self.modelA = MultinomialNB()

    def dictCleaning(self):
        dictionary = set()

        for i in self.nxDF:
            validWords = [self.stemmer.stem(nxDF) for nxDF in i if nxDF not in self.stopwords and len(nxDF) > 2]
            dictionary.update(validWords)

        dictionaryLen = len(dictionary)

        tuples = zip(dictionary, range(dictionaryLen))
        librarian = {word: i for word, i in tuples}

        return librarian

    def textVectorize(self, txt, librarian):
        vectorizedArray = [0] * len(librarian)
        for word in txt:
            if len(word) > 0:
                stem = self.stemmer.stem(word)
                if stem in librarian:
                    position = librarian[stem]
                    vectorizedArray[position] += 1

        return vectorizedArray

    def fit(self, librarian):
        txtVectors = [self.textVectorize(txt, librarian) for txt in self.nxDF]

        x = txtVectors
        y = self.yDF

        multinomial = self.modelA.fit(x, y)

        return multinomial

    def pred(self, multinomial, phrase):
        phrase = nltk.tokenize.word_tokenize(phrase)
        phrase = self.textVectorize(phrase, librarian)
        x = multinomial.predict([phrase])

        print(x[0].upper())


if __name__ == '__main__':
    o = NLTK()
    librarian = o.dictCleaning()
    multinomial = o.fit(librarian)

    while (True):
        phrase = input('Insira uma frase: ')
        o.pred(multinomial, phrase)
