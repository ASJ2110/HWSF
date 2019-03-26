# takes a list of weights only and returns a list of these weights after normalisation
def normaliseWeights(unnormalisedList):
    total = 0
    normalisedList = []
    for element in unnormalisedList:
        total += element
    for element in unnormalisedList:
        normalisedList.append(element/total)
    return normalisedList
