from typing import List
import numpy as np
from collections import Counter

class LandOfLogic:
    def __init__(self):
        self.ms_longestWord=self.longestWord(text='To be or not to be!')

    def longestWord(self,text):#does not work with special character
        keepLenght = 0
        lenOfSingeString = []
        splitedText = text.split(" ")
        for i in range(len(splitedText)):
            lenOfSingeString.append(len(splitedText[i]))
            if keepLenght < lenOfSingeString[i]:
                keepLenght = lenOfSingeString[i]
                index=lenOfSingeString.index(keepLenght)
        longWord=splitedText[index]
        return longWord


class RainbowOfClarity:
    def __init__(self):
        self.mb_isDigit = self.isDigit(symbol='6')

    def isDigit(self,symbol):
        digitOrNot = symbol.isdigit()
        return digitOrNot


class RainsOfReason:
    def __init__(self):
        self.mb_variableName=self.variableName(name='2w2')

    def variableName(self,name):#two hidden test failed but reveals it costs 10000
        candidate = True
        cond1 = list(range(ord('a'), ord('z')))
        cond2 = list(range(ord('A'), ord('Z')))
        cond3 = [95]
        if bool(name[0].isdigit())==True or name[0]==' ':
            return False
        for i in range(1,len(name)):
            if ord(name[i]) in cond1 + cond2 + cond3 or name[i].isdigit()==True:

                candidate = True
            else:
                candidate = False
                break
        return candidate

class DivingDeeper:
    def __init__(self):
        self.ms_firstDigit=self.firstDigit('var_1__Int')
        #self.ml_extractEachKth=self.extractEachKth(inputArray=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], k=3)

    def firstDigit(self,inputString):
        for i in range(len(inputString)):
            if bool(inputString[i].isdigit()==True):
                return inputString[i]

    def extractEachKth(self,inputArray, k):
        for j in range(1, len(inputArray)):
            f = lambda: k, inputArray.remove(k*j)
            mapped=list(map(f,inputArray))

        return mapped

class EruptionOfLight:

    def __init__(self):
        self.mb_beautifulString=self.isBeautifulString(inputString='bbc')

        
    def isBeautifulString(self, inputString):
        isBeautiful=True
        ls_input=list(inputString)
        ls_input.sort()

        dic={}
        for ch in ls_input:
            dic[ch]=dic.get(ch,0)+1
        for k in range(len(ls_input)-1):
            if dic[ls_input[k]]<=dic[ls_input[k+1]]:
                isBeautiful= False
        return isBeautiful








if __name__ == "__main__":
    land=LandOfLogic()
    rainbow=RainbowOfClarity()
    rain=RainsOfReason()
    diving=DivingDeeper()
    erruption=EruptionOfLight()
    print('the end')
