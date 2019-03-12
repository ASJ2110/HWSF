import Generate_feature_output

def sortList(unsortedList):
    isSorted = False
    while not isSorted:
        isSorted = True
        for i in range(len(unsortedList) - 1):
            if unsortedList[i][0] > unsortedList[i + 1][0]:
                store = unsortedList[i + 1]
                unsortedList[i + 1] = unsortedList[i]
                unsortedList[i] = store
                isSorted = False
    return lis
def calculateError(feature, thresholdValue):
    Tp = 0
    Tn = 0
    Sp = 0
    Sn = 0
    for i in range(thresholdValue):
        if feature[i][1] == 1:
            Sp += 1
            Tp += 1
        else:
            Sn += 1
            Tn += 1
    for i in range(len(feature)-thresholdValue):
        if feature[i+thresholdValue][1] == 1:
            Tp += 1
        else:
            Tn += 1
    if Tp-Sp+Sn < Tn-Sn+Sp:
        return Tp-Sp+Sn
    else:
        return Tn-Sn+Sp

lis = Generate_feature_output.generateFeatureOutput()
lis = sortList(lis)
optimalThreshold = 0
optimalThresholdError = len(lis)
for threshold in range(len(lis)):
    thresholdError = calculateError(lis, threshold)
    if thresholdError < optimalThresholdError:
        optimalThreshold = threshold
        optimalThresholdError = thresholdError
print(lis[optimalThreshold-1][0])#inclusive