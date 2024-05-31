import numpy as np
import copy

words = open("wordle_words.txt","r")
words = words.readlines()
words = [sub[: -1] for sub in words]
stillAllowed = words.copy()

pastWords = open("past_words.txt","r")
pastWords = pastWords.readlines()
pastWords = [sub[: -1] for sub in pastWords]
for i in range(len(pastWords)):
    pastWords[i] = pastWords[i].lower()
# print(pastWords)
# print(words)

global isNot, notNot, contains
isNot = [[],[],[],[],[]]
notNot = ["","","","",""]
contains = []

def updateKnown(guess,info):
    # guess is the word guessed and info represents the color of that letter (gray, yellow, or green)
    for i in range(5):
        l = guess[i]
        if (info[i] == "gray"):
            for i in range(5):
                if (notNot[i] == ""):
                    addToIsNot(i,l)
        elif (info[i] == "yellow"):
            addToIsNot(i,l)
            addToContains(l)
        elif (info[i] == "green"):
            addToNotNot(i,l)
            addToContains(l)

def addToIsNot(idx,letter):
    for i in isNot[idx]:
        if (i == letter):
            return
    isNot[idx].append(letter)

def addToNotNot(idx,letter):
    notNot[idx] = letter

def addToContains(letter):
    for i in contains:
        if (i == letter):
            return
    contains.append(letter)

def listContains(list,val):
    for i in list:
        if (i == val):
            return True
    return False

def isPossible(word):
    # check if all letters match notNot
    for i in range(5):
        if (notNot[i] == ""):
            continue
        if (word[i] != notNot[i]):
            return False
    # check if any letters are not allowed in that space
    for i in range(5):
        if (listContains(isNot[i],word[i])):
            return False
    # check if all knwon letters are in the word (yellows)
    for i in contains:
        if (listContains(word,i) == False):
            return False
    return True
vIsPossible = np.vectorize(isPossible)

def getPossibilities():
    global stillAllowed
    possibilities = stillAllowed.copy()
    # print(np.where(vIsPossible(possibilities) == True, False, True))
    mask = np.ma.masked_where(vIsPossible(np.array(possibilities)) == False, possibilities)
    # print(mask,possibilities)
    # possibilities = possibilities[mask]
    possibilities = np.ma.compressed(mask)
    stillAllowed = possibilities
    return possibilities

def getCombination(word,solution):
    combo = ["","","","",""]
    # if a letter matches, make it green
    for i in range(5):
        if (word[i] == solution[i]):
            combo[i] = "green"
    # if a letter occurs in the word and it isn't green, make it yellow, else, make it gray
    for i in range(5):
        if (combo[i] != ""):
            continue
        l = word[i]
        doesContains = False
        for j in range(5):
            if (solution[j] == l and combo[j] == ""):
                doesContains = True
        if (doesContains):
            combo[i] = "yellow"
        else:
            combo[i] = "gray"
    return combo

def getEntropy(word):
    # store current information
    global isNot,notNot,contains, stillAllowed
    cIsNot = copy.deepcopy(isNot)
    cNotNot = copy.deepcopy(notNot)
    cContains = copy.deepcopy(contains)
    cStillAllowed = copy.deepcopy(stillAllowed)
    possibilities = getPossibilities()
    # entropy is the amount of information gained
    entropy = 0
    numPossibilities = len(possibilities)
    for i in range(numPossibilities):
        # get the color combination for a possibility
        combo = getCombination(word,possibilities[i])
        updateKnown(word,combo)
        numNewPossibilities = len(getPossibilities())
        if (numNewPossibilities != 0):
            entropy -= np.log2(numNewPossibilities/numPossibilities)
        # restore original information
        globals()["isNot"] = copy.deepcopy(cIsNot)
        globals()["notNot"] = copy.deepcopy(cNotNot)
        globals()["contains"] = copy.deepcopy(cContains)
        globals()["stillAllowed"] = copy.deepcopy(cStillAllowed)
        # print(possibilities[i], str(i + 1) + "/" + str(numPossibilities), entropy)
    entropy /= numPossibilities
    return entropy

def getBestGuess():
    entropies = []
    i = 0
    for word in pastWords:
        entropies.append(getEntropy(word))
        i += 1
        print(str(i) + "/" + str(len(pastWords)))
    return pastWords[entropies.index(max(entropies))]

# stillAllowed = pastWords
updateKnown("stare",["gray","gray","gray","gray","yellow"])
# updateKnown("knelt",["gray","yellow","gray","gray","gray"])
# updateKnown("tabus",["gray","gray","gray","gray","gray"])
# updateKnown("chace",["gray","gray","gray","gray","gray"])
# updateKnown("donor",["gray","green","yellow","green","yellow"])
print(getPossibilities())
# print(getEntropy("other"))
# print(isNot, vIsPossible(["chaos"]))
# print(getEntropy("cigar"))
# print(len(getPossibilities()))
# print(getEntropy("chace"))
print(getBestGuess())