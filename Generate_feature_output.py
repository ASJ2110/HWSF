import math
import random
def generateFeatureOutput():
    ret = []
    for i in range(50):
        featureVal = math.floor(random.gauss(100, 80))
        pos = 0
        if featureVal > 100:
            pos = 1
        featureVal += math.floor(random.gauss(0, 20))
        ret.append([featureVal, pos])
    return ret