#!-*- coding: utf8 -*-
from __future__ import division
from sklearn.model_selection import cross_val_score
from sklearn.multiclass import OneVsRestClassifier
from sklearn.multiclass import OneVsOneClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import LinearSVC
from collections import Counter
import pandas
import numpy
import nltk

dataFrame = pandas.read_csv("/Users/brunopaes/Documents/OneDrive/Acadêmico/ESPM/Projetos/Microagression/data/Book1.csv", encoding = "utf-8")

xDF = dataFrame['microagression']
lowerText = xDF.str.lower()
stopwords = nltk.corpus.stopwords.words("portuguese")
stemmer = nltk.stem.RSLPStemmer()
nxDF = [nltk.tokenize.word_tokenize(i) for i in lowerText]

dictionary = set()
for i in nxDF:
    validWords = [stemmer.stem(nxDF) for nxDF in i if nxDF not in stopwords and len(nxDF) > 2]
    dictionary.update(validWords)

tuples = zip(dictionary, range(len(dictionary)))
librarian = {word: i for word, i in tuples}


def textVectorize(txt, librarian):
    vectorizedArray = [0] * len(librarian)
    for word in txt:
        if len(word) > 0:
            stem = stemmer.stem(word)
            if stem in librarian:
                position = librarian[stem]
                vectorizedArray[position] += 1

    return vectorizedArray


txtVectors = [textVectorize(txt, librarian) for txt in nxDF]

yDF = dataFrame['class']

x = txtVectors
y = yDF

assertivenessRate = float(0)
assertivenessBase = float(0)
assertiveness = float(0)

trainPercentage = 0.8

trainLen = int(trainPercentage * len(y))
valLen = len(y) - trainLen

xTraining = x[:trainLen]
yTraining = y[:trainLen]

xVal = x[trainLen:]
yVal = y[trainLen:]


def fitAndPredict(name, model, xTraining, yTrain):
    k = 2
    scores = cross_val_score(model, xTraining, yTrain, cv = k)
    assertivenessRate = numpy.mean(scores) * 100

    print("The algorithm '{0}' has: {1:.2f} % of assertiveness rate".format(name, assertivenessRate))

    return assertivenessRate


def validationDumbAlgorithm(assertivenessBase, yVal):
    assertivenessBase = max(Counter(yVal).values())
    assertivenessBase = 100.0 * assertivenessBase / len(yVal)

    print("Identity Algorithm Assertiveness Rate: {0:.2f} %".format(assertivenessBase))


def modelValidation(model, xVal, yVal):
    result = model.predict(xVal)
    points = result == yVal
    assertivenessRate = 100.0 * sum(points) / len(yVal)

    print("In the validation process the winner algorithm achieved an assertiveness rate of: {0:.2f} %".format(assertivenessRate))


validationDumbAlgorithm(assertivenessBase, yVal)

resultDictionaries = {}

modelA = MultinomialNB()
multinomial = fitAndPredict("multinomial", modelA, xTraining, yTraining)
resultDictionaries[multinomial] = modelA

modelB = AdaBoostClassifier(random_state = 0)
adaboost = fitAndPredict("adaboost", modelB, xTraining, yTraining)
resultDictionaries[adaboost] = modelB

modelC = OneVsRestClassifier(LinearSVC(random_state = 0))
ovsr = fitAndPredict("ovsr", modelC, xTraining, yTraining)
resultDictionaries[ovsr] = modelC

modelD = OneVsOneClassifier(LinearSVC(random_state = 0))
ovso = fitAndPredict("ovso", modelD, xTraining, yTraining)
resultDictionaries[ovso] = modelD

max = max(resultDictionaries)
winner = resultDictionaries[max]

winner.fit(xTraining, yTraining)
result = winner.predict(xVal)
points = result == yVal

modelValidation(winner, xVal, yVal)
