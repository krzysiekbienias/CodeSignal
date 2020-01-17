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
        self.mb_variableName=self.variableName(name='var_1__Int')

    def variableName(self,name):
        candidate = True
        cond1 = list(range(ord('a'), ord('z')))
        cond2 = list(range(ord('A'), ord('Z')))
        cond3 = [95]
        for i in range(len(name)):
            if ord(name[i]) in cond1 + cond2 + cond3:

                candidate = True
            else:
                candidate = False
                break
        return candidate


if __name__ == "__main__":
    land=LandOfLogic()
    rainbow=RainbowOfClarity()
    rain=RainsOfReason()
    print('the end')
