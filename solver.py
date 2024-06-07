import numpy as np
import copy

words = open("wordle_words.txt","r")
words = words.readlines()
words = [sub[: -1] for sub in words]
stillAllowed = words.copy()

smallList = open("small_list.txt","r")
smallList = smallList.readlines()
smallList = [sub[: -1] for sub in smallList]
for i in range(len(smallList)):
    smallList[i] = smallList[i].lower()
# print(smallList)
# print(words)

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
            if (solution[j] == l and combo[i] == ""):
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
        # print(possibilities[i], str(i + 1) + "/" + str(numPossibilities), entropy/i)
    entropy /= numPossibilities
    return entropy

def getBestGuess(list):
    entropies = []
    i = 0
    possibilities = getPossibilities()
    # loop through all words and get their entropy
    if (len(possibilities) == 1):
        return possibilities[0]
    for word in list:
        entropies.append(getEntropy(word))
        i += 1
        # print current word and progress since this function takes a while to run
        print(str(i) + "/" + str(len(list)))
    # sort the words by their entropy
    nList = np.array(list)[np.flip(np.argsort(entropies,None,kind="quicksort"))]
    entropies = np.flip(np.sort(entropies,None,kind="quicksort"))
    # print words in decending order of entropy
    for i in range(len(entropies)):
        print(nList[i] + ": " + str(np.round(entropies[i] * 100)/100) + " bits")
    # return the word with the highest entropy
    return nList[0]
    # return stillAllowed[entropies.index(max(entropies))]

def getFreqOfCharacters(list):
    a = np.zeros(26)
    b = np.arange(26)
    for word in list:
        for letter in word:
            a[ord(letter)-97] += 1

    c = np.array(b)[np.flip(np.argsort(a,None,kind="quicksort"))]
    d = np.flip(np.sort(a,None,kind="quicksort"))
    print(c,d)
    for i in range(26):
        print(chr(c[i]+97) + ": " + str(d[i]))

stillAllowed = smallList

# functions:
# getFreqOfCharacters(list)
# getPossibilities()
# isPossible(word)
# updateKnown(guess,info)
# getEntropy(word)
# getBestGuess()

# updateKnown("roate",[""])
# print(getPossibilities())
# print(len(getPossibilities()))
# print(notNot,isNot,contains)
# print("Entropy of 'greet': " + str(getEntropy("greet")))
# print(len(smallList))
print("Best guess: " + getBestGuess(smallList))